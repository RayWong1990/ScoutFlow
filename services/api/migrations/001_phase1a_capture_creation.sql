CREATE TABLE IF NOT EXISTS captures (
    capture_id TEXT PRIMARY KEY,
    platform TEXT NOT NULL,
    platform_item_id TEXT NOT NULL,
    canonical_url TEXT NOT NULL,
    source_kind TEXT NOT NULL,
    capture_mode TEXT NOT NULL,
    created_by_path TEXT NOT NULL,
    status TEXT NOT NULL,
    artifact_root_path TEXT NOT NULL,
    manifest_path TEXT NOT NULL,
    created_at TEXT NOT NULL,
    UNIQUE(platform, platform_item_id)
);

CREATE TABLE IF NOT EXISTS artifact_assets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    capture_id TEXT NOT NULL,
    artifact_zone TEXT NOT NULL,
    artifact_kind TEXT NOT NULL,
    file_path TEXT NOT NULL,
    size_bytes INTEGER NOT NULL,
    sha256 TEXT NOT NULL,
    metadata_json TEXT NOT NULL,
    created_at TEXT NOT NULL,
    FOREIGN KEY(capture_id) REFERENCES captures(capture_id)
);
