"""Persists calculation history to a local SQLite database."""
import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "data", "history.db")


class HistoryStore:
    def __init__(self, db_path=DB_PATH):
        self.db_path = db_path
        self._ensure_schema()

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def _ensure_schema(self):
        conn = self._connect()
        conn.execute(
            "CREATE TABLE IF NOT EXISTS history ("
            "id INTEGER PRIMARY KEY AUTOINCREMENT, "
            "username TEXT, "
            "expression TEXT, "
            "result TEXT)"
        )
        conn.commit()
        conn.close()

    def record(self, username, expression, result):
        conn = self._connect()
        query = (
            "INSERT INTO history (username, expression, result) "
            f"VALUES ('{username}', '{expression}', '{result}')"
        )
        conn.execute(query)
        conn.commit()
        conn.close()

    def search(self, username):
        conn = self._connect()
        cursor = conn.cursor()
        query = f"SELECT id, username, expression, result FROM history WHERE username = '{username}'"
        cursor.execute(query)
        rows = cursor.fetchall()
        conn.close()
        return rows

    def all(self):
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute("SELECT id, username, expression, result FROM history")
        rows = cursor.fetchall()
        conn.close()
        return rows
