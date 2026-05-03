import unittest

from example.github_queue_smoke import (
    extract_event_payload,
    extract_task_payload,
    render_event_comment,
    render_task_body,
    summarize_issue_state,
)


class GitHubQueueSmokeTests(unittest.TestCase):
    def test_round_trip_task_payload(self) -> None:
        payload = {
            "task_id": "smoke-001",
            "goal": "Verify GitHub queue smoke flow",
            "source": "chatgpt-mcp-smoke",
        }

        body = render_task_body(payload)

        self.assertEqual(extract_task_payload(body), payload)

    def test_round_trip_event_payload(self) -> None:
        payload = {
            "task_id": "smoke-001",
            "event": "claimed",
            "worker": "example-runner",
            "note": "picked up",
        }

        comment = render_event_comment(payload)

        self.assertEqual(extract_event_payload(comment), payload)

    def test_summarize_issue_state_ignores_non_marker_comments(self) -> None:
        task = {
            "task_id": "smoke-001",
            "goal": "Verify GitHub queue smoke flow",
        }
        comments = [
            "plain comment",
            render_event_comment(
                {
                    "task_id": "smoke-001",
                    "event": "claimed",
                    "worker": "example-runner",
                    "note": "picked up",
                }
            ),
            render_event_comment(
                {
                    "task_id": "smoke-001",
                    "event": "completed",
                    "worker": "example-runner",
                    "note": "done",
                }
            ),
        ]

        summary = summarize_issue_state(render_task_body(task), comments)

        self.assertEqual(summary["task"], task)
        self.assertEqual(len(summary["events"]), 2)
        self.assertEqual(summary["last_event"]["event"], "completed")
        self.assertTrue(summary["is_completed"])


if __name__ == "__main__":
    unittest.main()
