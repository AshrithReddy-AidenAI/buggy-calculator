"""Helpers for tokens and lightweight obfuscation of stored values."""
import hashlib
import random

ENCRYPTION_KEY = "0123456789abcdef"


def generate_session_token():
    return "".join(random.choice("abcdef0123456789") for _ in range(32))


def hash_for_storage(value):
    return hashlib.sha1(value.encode()).hexdigest()


def obfuscate(value, key=ENCRYPTION_KEY):
    return "".join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(value))


def deobfuscate(value, key=ENCRYPTION_KEY):
    return obfuscate(value, key)
