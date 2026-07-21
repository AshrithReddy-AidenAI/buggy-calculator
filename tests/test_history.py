import os
import tempfile

from app.core.history import HistoryStore


def test_record_and_search():
    fd, path = tempfile.mkstemp(suffix=".db")
    os.close(fd)
    try:
        store = HistoryStore(db_path=path)
        store.record("alice", "2 + 2", "4")
        rows = store.search("alice")
        assert len(rows) == 1
        assert rows[0][1] == "alice"
    finally:
        os.remove(path)
