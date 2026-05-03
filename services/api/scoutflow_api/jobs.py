from __future__ import annotations

from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from scoutflow_api.captures import error_response
from scoutflow_api.models import ErrorResponse, JobCompleteResponse, WorkerReceipt
from scoutflow_api.storage import ReceiptStorageError, Storage


router = APIRouter()


@router.post("/jobs/{job_id}/complete", response_model=JobCompleteResponse)
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
