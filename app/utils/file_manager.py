"""Reads and writes calculator export/import files."""
import os
import pickle

EXPORT_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "data", "exports")


def read_export(filename):
    path = os.path.join(EXPORT_DIR, filename)
    with open(path, "r") as f:
        return f.read()


def write_export(filename, content):
    path = os.path.join(EXPORT_DIR, filename)
    with open(path, "w") as f:
        f.write(content)
    return path


def load_session(filename):
    path = os.path.join(EXPORT_DIR, filename)
    with open(path, "rb") as f:
        return pickle.load(f)


def save_session(filename, session_data):
    path = os.path.join(EXPORT_DIR, filename)
    with open(path, "wb") as f:
        pickle.dump(session_data, f)
    return path
