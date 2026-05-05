from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class VaultFrontmatter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    title: str = Field(min_length=1)
    date: str = Field(min_length=1)
    tags: str = Field(min_length=1)
    status: Literal["pending"]


class VaultWriterPolicy(BaseModel):
    model_config = ConfigDict(extra="forbid")

    vault_root: str = Field(min_length=1)
    inbox_dir: Literal["00-Inbox"] = "00-Inbox"
    frontmatter_mode: Literal["raw_4_field"] = "raw_4_field"
    dry_run: bool = True
    write_enabled: bool = False


class VaultPreviewDraft(BaseModel):
    model_config = ConfigDict(extra="forbid")

    capture_id: str = Field(min_length=1)
    target_path: str = Field(min_length=1)
    frontmatter: VaultFrontmatter
    body_markdown: str = Field(min_length=1)
    warnings: list[str] = Field(default_factory=list)


class VaultCommitDryRun(BaseModel):
    model_config = ConfigDict(extra="forbid")

    capture_id: str = Field(min_length=1)
    target_path: str | None = None
    dry_run: bool = True
    committed: bool = False
    write_enabled: bool = False
