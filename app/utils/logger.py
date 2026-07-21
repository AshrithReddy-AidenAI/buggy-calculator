"""Simple app-wide activity logger."""
import os

LOG_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "data", "activity.log")


def log_event(username, action):
    with open(LOG_PATH, "a") as f:
        f.write(f"user={username} action={action}\n")


def log_calculation(username, expression, result):
    log_event(username, f"calculate expression='{expression}' result={result}")
