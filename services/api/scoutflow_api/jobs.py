from __future__ import annotations

from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from scoutflow_api.captures import error_response
from scoutflow_api.models import ErrorResponse, JobCompleteResponse, WorkerReceipt
from scoutflow_api.storage import ReceiptStorageError, Storage


router = APIRouter(tags=["jobs"])


@router.post(
    "/jobs/{job_id}/complete",
    response_model=JobCompleteResponse,
    summary="Complete job (worker callback)",
    description=(
        "Worker submits a `WorkerReceipt` to mark a job succeeded or failed. "
        "Completion is idempotent on receipt content and does not advance capture state "
        "beyond what the receipt prescribes."
    ),
    responses={
        404: {"model": ErrorResponse, "description": "Rejected with `job_not_found` or `capture_not_found`."},
        409: {
            "model": ErrorResponse,
            "description": (
                "Rejected with one of: `job_capture_mismatch`, `job_type_mismatch`, "
                "`job_dedupe_key_mismatch`, `next_status_not_supported`, "
                "`capture_state_conflict`, `idempotent_platform_result_conflict`, "
                "`idempotent_ledger_missing`, `idempotent_ledger_conflict`, or "
                "`artifact_ledger_conflict`."
            ),
        },
        422: {
            "model": ErrorResponse,
            "description": (
                "Rejected with `job_id_mismatch`, `artifact_path_outside_root`, "
                "`artifact_file_missing`, `artifact_bytes_mismatch`, or "
                "`artifact_sha256_mismatch`."
            ),
        },
    },
)
def complete_job(job_id: str, payload: WorkerReceipt, request: Request) -> JobCompleteResponse | JSONResponse:
    if job_id != payload.job_id:
        return error_response(422, "job_id_mismatch", "Path job_id must match receipt job_id.")

    storage: Storage = request.app.state.storage
    try:
        completed = storage.complete_job_receipt(payload)
    except ReceiptStorageError as exc:
        body = ErrorResponse(code=exc.code, message=exc.message).model_dump()
        return JSONResponse(status_code=exc.http_status, content=body)

    return JobCompleteResponse(**completed)
