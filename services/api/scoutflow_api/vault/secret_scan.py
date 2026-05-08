from __future__ import annotations

import re
from collections.abc import Iterable

from scoutflow_api.vault.schemas import (
    VaultSecretScanMatch,
    VaultSecretScanPattern,
    VaultSecretScanReport,
)


SURFACES = [
    "frontmatter_candidate",
    "markdown_body",
    "canonical_url",
    "trust_trace_notes",
    "rewrite_output",
    "transcript_handoff",
    "receipt_manifest_material",
]

PATTERN_RULES: dict[VaultSecretScanPattern, re.Pattern[str]] = {
    VaultSecretScanPattern.cookie: re.compile(r"\bcookie\b", re.IGNORECASE),
    VaultSecretScanPattern.token: re.compile(r"\btoken\b", re.IGNORECASE),
    VaultSecretScanPattern.api_key: re.compile(r"\bapi[_-]?key\b", re.IGNORECASE),
    VaultSecretScanPattern.authorization_header: re.compile(r"\bauthorization\s*:", re.IGNORECASE),
    VaultSecretScanPattern.signed_media_url: re.compile(r"(signature=|sig=|x-amz-signature=)", re.IGNORECASE),
    VaultSecretScanPattern.raw_stdout_stderr: re.compile(r"\b(stdout|stderr)\b", re.IGNORECASE),
    VaultSecretScanPattern.auth_sidecar: re.compile(r"\b(bbdown\.data|cookies?\.txt|auth[_-]?sidecar)\b", re.IGNORECASE),
    VaultSecretScanPattern.browser_profile_path: re.compile(r"(~/Library/Application Support/|/Default/|/Profile \d+/)"),
    VaultSecretScanPattern.local_credential_path: re.compile(r"(\.aws/|\.config/gcloud|\.netrc|id_rsa|credentials)", re.IGNORECASE),
}


def build_secret_scan_report(
    *,
    frontmatter_candidate: str,
    markdown_body: str,
    canonical_url: str,
    trust_trace_notes: str,
    rewrite_output: str,
    transcript_handoff: str,
    receipt_manifest_material: str,
) -> VaultSecretScanReport:
    surface_values = {
        "frontmatter_candidate": frontmatter_candidate,
        "markdown_body": markdown_body,
        "canonical_url": canonical_url,
        "trust_trace_notes": trust_trace_notes,
        "rewrite_output": rewrite_output,
        "transcript_handoff": transcript_handoff,
        "receipt_manifest_material": receipt_manifest_material,
    }
    matches: list[VaultSecretScanMatch] = []
    for surface, text in surface_values.items():
        matches.extend(_scan_surface(surface, text))

    return VaultSecretScanReport(
        surfaces_checked=list(SURFACES),
        blocking_categories=list(PATTERN_RULES),
        blocked=bool(matches),
        matches=matches,
    )


def _scan_surface(surface: str, text: str) -> Iterable[VaultSecretScanMatch]:
    location_class = f"{surface}_surface"
    for category, pattern in PATTERN_RULES.items():
        if pattern.search(text):
            yield VaultSecretScanMatch(
                category=category,
                surface=surface,
                location_class=location_class,
            )
