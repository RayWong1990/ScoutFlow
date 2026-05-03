from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class DiscoverCaptureRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    platform: str
    canonical_url: str
    source_kind: str
    quick_capture_preset: str


class DiscoverCaptureResponse(BaseModel):
    capture_id: str
    platform: str
    platform_item_id: str
    source_kind: str
    capture_mode: str
    created_by_path: str
    status: str
    artifact_root_path: str
    manifest_path: str


class ErrorResponse(BaseModel):
    code: str
    message: str
