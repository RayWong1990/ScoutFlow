from __future__ import annotations

from dataclasses import dataclass

from fastapi.responses import JSONResponse

from scoutflow_api.bridge.schemas import BridgeErrorCode
from scoutflow_api.models import ErrorResponse


@dataclass(frozen=True)
class BridgeRouteError(Exception):
    status_code: int
    code: BridgeErrorCode
    message: str

    def __str__(self) -> str:
        return f"{self.code.value}: {self.message}"


def bridge_error_response(status_code: int, code: BridgeErrorCode, message: str) -> JSONResponse:
    body = ErrorResponse(code=code.value, message=message).model_dump()
    return JSONResponse(status_code=status_code, content=body)
