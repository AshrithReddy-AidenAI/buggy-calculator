# buggy-calculator

A test fixture used to exercise an autonomous bug-fixing / vulnerability-fixing
agent. Do not use in production — it intentionally contains logic bugs and
security issues (SQL injection, command injection, hardcoded secrets, weak
crypto, path traversal, insecure deserialization, etc.) spread across a small
multi-module Flask app.

## Layout

- `app/core/` — calculator logic (`operations.py`), calculation history
  persisted to SQLite (`history.py`), and a minimal auth store (`auth.py`).
- `app/api/` — Flask HTTP API (`server.py`) exposing calculate/history/login/
  admin/export endpoints.
- `app/utils/` — crypto helpers, file import/export, and activity logging.
- `app/cli.py` — command-line entry point for running expressions.
- `app/config.py` — app configuration.
- `tests/` — pytest suite.
- `calculator.py` — thin backwards-compatible shim over `app.core.operations`.

## Running

```
pip install -r requirements.txt
pytest
python -m app.api.server
```
