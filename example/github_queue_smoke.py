#!/usr/bin/env python3
"""Minimal GitHub-backed smoke flow for scheme C."""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path
from typing import Any

TASK_MARKER = "<!-- scoutflow-c-smoke-task:v1 -->"
EVENT_MARKER = "<!-- scoutflow-c-smoke-event:v1 -->"


def render_task_body(payload: dict[str, Any]) -> str:
    return f"{TASK_MARKER}\n{json.dumps(payload, ensure_ascii=False, indent=2)}\n"


def extract_task_payload(text: str) -> dict[str, Any]:
    return _extract_payload(text, TASK_MARKER)


def render_event_comment(payload: dict[str, Any]) -> str:
    return f"{EVENT_MARKER}\n{json.dumps(payload, ensure_ascii=False, indent=2)}\n"


def extract_event_payload(text: str) -> dict[str, Any]:
    return _extract_payload(text, EVENT_MARKER)


def summarize_issue_state(issue_body: str, comment_bodies: list[str]) -> dict[str, Any]:
    task = extract_task_payload(issue_body)
    events = []
    for body in comment_bodies:
        if EVENT_MARKER not in body:
            continue
        events.append(extract_event_payload(body))
    last_event = events[-1] if events else None
    return {
        "task": task,
        "events": events,
        "last_event": last_event,
        "is_completed": bool(last_event and last_event.get("event") == "completed"),
    }


def gh(repo: str, *args: str) -> str:
    cmd = ["gh", *args, "--repo", repo]
    result = subprocess.run(cmd, check=True, capture_output=True, text=True)
    return result.stdout.strip()


def enqueue(repo: str, task_file: Path, title: str | None) -> dict[str, Any]:
    payload = json.loads(task_file.read_text())
    issue_title = title or f"[scheme-c-smoke] {payload['task_id']}"
    issue_body = render_task_body(payload)
    url = gh(repo, "issue", "create", "--title", issue_title, "--body", issue_body)
    return {"task": payload, "url": url}


def read_issue(repo: str, issue: str) -> dict[str, Any]:
    raw = gh(repo, "issue", "view", issue, "--json", "number,title,body,url,comments")
    data = json.loads(raw)
    comment_bodies = [comment["body"] for comment in data.get("comments", [])]
    summary = summarize_issue_state(data["body"], comment_bodies)
    data["summary"] = summary
    return data


def comment_event(repo: str, issue: str, payload: dict[str, Any]) -> None:
    gh(repo, "issue", "comment", issue, "--body", render_event_comment(payload))


def run_worker(repo: str, issue: str, worker: str) -> dict[str, Any]:
    data = read_issue(repo, issue)
    task = data["summary"]["task"]
    events = data["summary"]["events"]

    if any(event.get("event") == "completed" for event in events):
        return {
            "issue": data["url"],
            "task_id": task["task_id"],
            "status": "already_completed",
        }

    comment_event(
        repo,
        issue,
        {
            "task_id": task["task_id"],
            "event": "claimed",
            "worker": worker,
            "note": "runner picked up smoke task",
        },
    )
    comment_event(
        repo,
        issue,
        {
            "task_id": task["task_id"],
            "event": "completed",
            "worker": worker,
            "note": "runner completed smoke task without product-side effects",
        },
    )

    return {
        "issue": data["url"],
        "task_id": task["task_id"],
        "status": "completed",
    }


def inspect(repo: str, issue: str) -> dict[str, Any]:
    data = read_issue(repo, issue)
    return {
        "issue": data["url"],
        "task": data["summary"]["task"],
        "events": data["summary"]["events"],
        "is_completed": data["summary"]["is_completed"],
    }


def _extract_payload(text: str, marker: str) -> dict[str, Any]:
    if marker not in text:
        raise ValueError(f"marker not found: {marker}")
    payload_text = text.split(marker, 1)[1].strip()
    return json.loads(payload_text)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Minimal GitHub queue smoke flow")
    subparsers = parser.add_subparsers(dest="command", required=True)

    enqueue_parser = subparsers.add_parser("enqueue")
    enqueue_parser.add_argument("--repo", required=True)
    enqueue_parser.add_argument("--task-file", required=True, type=Path)
    enqueue_parser.add_argument("--title")

    run_parser = subparsers.add_parser("run")
    run_parser.add_argument("--repo", required=True)
    run_parser.add_argument("--issue", required=True)
    run_parser.add_argument("--worker", default="example-runner")

    inspect_parser = subparsers.add_parser("inspect")
    inspect_parser.add_argument("--repo", required=True)
    inspect_parser.add_argument("--issue", required=True)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "enqueue":
        result = enqueue(args.repo, args.task_file, args.title)
    elif args.command == "run":
        result = run_worker(args.repo, args.issue, args.worker)
    else:
        result = inspect(args.repo, args.issue)

    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
