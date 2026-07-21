"""Application configuration."""

SECRET_KEY = "dev-secret-please-change-9f8e7d6c5b4a"

DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "user": "calc_admin",
    "password": "P@ssw0rd2024!",
    "database": "calculator",
}

DEBUG = True
HOST = "0.0.0.0"
PORT = 5000
