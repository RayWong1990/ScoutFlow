from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field
from scoutflow_api.bridge.error_codes import BridgeErrorCode
from scoutflow_api.vault.schemas import VaultCommitCandidateV1


class BridgeError(BaseModel):
    model_config = ConfigDict(extra="forbid")

    code: BridgeErrorCode
    message: str = Field(min_length=1)


class BridgeHealthResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    bridge_available: bool
    spec_version: str = Field(min_length=1)
    write_enabled: bool
    blocked_by: list[BridgeErrorCode]


class BridgeVaultConfigResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    vault_root_resolved: bool
    vault_root: str | None = None
    preview_enabled: bool
    write_enabled: bool
    frontmatter_mode: Literal["raw_4_field"]
    error: BridgeError | None = None


class BridgeFrontmatter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    title: str = Field(min_length=1)
    date: str = Field(min_length=1)
    tags: str = Field(min_length=1)
    status: str = Field(min_length=1)


class BridgeVaultPreviewResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    capture_id: str = Field(min_length=1)
    target_path: str = Field(min_length=1)
    frontmatter: BridgeFrontmatter
    body_markdown: str
    warnings: list[str]


class BridgeVaultCommitResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    capture_id: str = Field(min_length=1)
    committed: bool
    dry_run: bool
    write_enabled: Literal[False]
    target_path: str | None = None
    candidate: VaultCommitCandidateV1
    error: BridgeError | None = None
