from __future__ import annotations

import os
from collections.abc import Mapping

from scoutflow_api.bridge.error_codes import BridgeErrorCode
from scoutflow_api.vault.schemas import VaultWriterPolicy


SCOUTFLOW_VAULT_ROOT_ENV = "SCOUTFLOW_VAULT_ROOT"
VAULT_INBOX_DIR = "00-Inbox"
RAW_FRONTMATTER_MODE = "raw_4_field"
DEFAULT_FRONTMATTER_TAGS = "调研/ScoutFlow采集"
DEFAULT_FRONTMATTER_STATUS = "pending"


class VaultWriterError(RuntimeError):
    def __init__(self, code: BridgeErrorCode, message: str) -> None:
        super().__init__(message)
        self.code = code
        self.message = message


def resolve_required_vault_root(env: Mapping[str, str] | None = None) -> str:
    env_map = os.environ if env is None else env
    vault_root = env_map.get(SCOUTFLOW_VAULT_ROOT_ENV, "").strip()
    if not vault_root:
        raise VaultWriterError(
            BridgeErrorCode.vault_root_unset,
            "SCOUTFLOW_VAULT_ROOT is not configured.",
        )
    return vault_root


def build_writer_policy(env: Mapping[str, str] | None = None) -> VaultWriterPolicy:
    return VaultWriterPolicy(vault_root=resolve_required_vault_root(env))
