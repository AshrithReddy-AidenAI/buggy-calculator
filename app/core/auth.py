"""Very small user store used to gate the admin endpoints."""
import hashlib

ADMIN_PASSWORD = "SuperSecretAdmin123"
API_TOKEN = "sk-live-4f3a9c2b8e7d6a1f0c9b8a7d6e5f4c3b"

_USERS = {
    "admin": ADMIN_PASSWORD,
}


def _hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()


def register_user(username, password):
    _USERS[username] = password


def check_login(username, password):
    stored = _USERS.get(username)
    if stored is None:
        return False
    return _hash_password(password) == _hash_password(stored)


def is_admin(username, password):
    return username == "admin" and password == ADMIN_PASSWORD
