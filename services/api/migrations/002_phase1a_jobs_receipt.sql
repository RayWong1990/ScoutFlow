CREATE TABLE IF NOT EXISTS jobs (
    job_id TEXT PRIMARY KEY,
    capture_id TEXT NOT NULL,
    job_type TEXT NOT NULL,
    status TEXT NOT NULL,
    dedupe_key TEXT NOT NULL,
    queued_at TEXT NOT NULL,
    started_at TEXT,
    completed_at TEXT,
    platform_result TEXT,
    last_error_json TEXT,
    UNIQUE(job_id),
    FOREIGN KEY(capture_id) REFERENCES captures(capture_id)
);

CREATE TABLE IF NOT EXISTS job_events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    job_id TEXT NOT NULL,
    event_type TEXT NOT NULL,
    event_json TEXT NOT NULL,
    created_at TEXT NOT NULL,
    FOREIGN KEY(job_id) REFERENCES jobs(job_id)
);

CREATE INDEX IF NOT EXISTS idx_jobs_capture ON jobs(capture_id);
CREATE INDEX IF NOT EXISTS idx_jobs_status ON jobs(status);
CREATE INDEX IF NOT EXISTS idx_jobs_type_status ON jobs(job_type, status);
CREATE UNIQUE INDEX IF NOT EXISTS idx_jobs_capture_type_dedupe
ON jobs(capture_id, job_type, dedupe_key);
CREATE INDEX IF NOT EXISTS idx_job_events_job_id ON job_events(job_id);
CREATE UNIQUE INDEX IF NOT EXISTS idx_artifact_assets_capture_file
ON artifact_assets(capture_id, file_path);
