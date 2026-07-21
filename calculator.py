"""Backwards-compatible entry point; real implementation lives in app/core/operations.py."""
from app.core.operations import (
    add,
    subtract,
    multiply,
    divide,
    power,
    average,
    factorial,
    is_prime,
    square_root,
    percentage,
)

__all__ = [
    "add",
    "subtract",
    "multiply",
    "divide",
    "power",
    "average",
    "factorial",
    "is_prime",
    "square_root",
    "percentage",
]
