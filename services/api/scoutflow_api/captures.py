from __future__ import annotations

import re
from urllib.parse import ParseResult, urlparse

from fastapi import APIRouter, Request, status
from fastapi.responses import JSONResponse

from scoutflow_api.models import DiscoverCaptureRequest, DiscoverCaptureResponse, ErrorResponse
from scoutflow_api.storage import Storage


BV_ID_RE = re.compile(r"(BV[0-9A-Za-z]{10})")
LP001_REJECTED_SOURCE_KINDS = {"recommendation", "keyword", "raw_gap"}
SUPPORTED_PLATFORM = "bilibili"
SUPPORTED_SCHEMES = {"http", "https"}

router = APIRouter()


def error_response(http_status: int, code: str, message: str) -> JSONResponse:
    body = ErrorResponse(code=code, message=message).model_dump()
    return JSONResponse(status_code=http_status, content=body)


def is_bilibili_host(parsed: ParseResult) -> bool:
    host = parsed.hostname
    if host is None:
        return False
    normalized = host.lower().rstrip(".")
    return normalized == "bilibili.com" or normalized.endswith(".bilibili.com")


def extract_bilibili_bv_id(canonical_url: str) -> str | None:
    parsed = urlparse(canonical_url)
    if parsed.scheme.lower() not in SUPPORTED_SCHEMES or not is_bilibili_host(parsed):
        return None
    match = BV_ID_RE.search(parsed.path)
    return match.group(1) if match else None


@router.post("/captures/discover", response_model=DiscoverCaptureResponse, status_code=status.HTTP_201_CREATED)
def create_capture(payload: DiscoverCaptureRequest, request: Request) -> DiscoverCaptureResponse | JSONResponse:
    if payload.platform != SUPPORTED_PLATFORM:
        return error_response(422, "unsupported_platform", "T-P1A-001 only supports bilibili.")

    if payload.source_kind in LP001_REJECTED_SOURCE_KINDS:
        return error_response(
            422,
            "lp001_direct_capture_forbidden",
            "recommendation / keyword / RAW gap cannot directly create capture.",
        )

    if payload.source_kind != "manual_url":
        return error_response(422, "source_kind_not_allowed", "Only manual_url is allowed in T-P1A-001.")

    if payload.quick_capture_preset == "audio_transcript":
        return error_response(
            422,
            "not_implemented_in_T-P1A-001",
            "audio_transcript runtime is out of scope for T-P1A-001.",
        )

    if payload.quick_capture_preset != "metadata_only":
        return error_response(422, "invalid_quick_capture_preset", "Only metadata_only is supported.")

    platform_item_id = extract_bilibili_bv_id(payload.canonical_url)
    if platform_item_id is None:
        parsed = urlparse(payload.canonical_url)
        if not is_bilibili_host(parsed):
            return error_response(422, "unsupported_platform", "canonical_url must be a bilibili URL.")
        if parsed.scheme.lower() not in SUPPORTED_SCHEMES:
            return error_response(422, "invalid_bilibili_url", "canonical_url must use http or https.")
        return error_response(422, "invalid_bilibili_url", "canonical_url must contain a BV id.")

    storage: Storage = request.app.state.storage
    created = storage.create_metadata_capture(payload.canonical_url, platform_item_id)
    return DiscoverCaptureResponse(**created)
