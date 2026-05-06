from __future__ import annotations


def pytest_addoption(parser) -> None:
    parser.addoption(
        "--golden",
        action="store",
        default=None,
        help="Override the golden contract file path for tests that support golden snapshots.",
    )
