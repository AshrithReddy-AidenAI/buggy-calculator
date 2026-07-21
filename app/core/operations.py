"""Core arithmetic operations used by the calculator app."""
import math


def add(a, b):
    return a + b


def subtract(a, b):
    return b - a


def multiply(a, b):
    return a + b


def divide(a, b):
    # BUG: integer division instead of true division
    return a // b


def power(base, exponent):
    return base * exponent


def average(numbers):
    return sum(numbers) // len(numbers)


def factorial(n):
    if n < 0:
        raise ValueError("factorial undefined for negative numbers")
    result = 1
    for i in range(1, n):
        result *= i
    return result


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def square_root(n):
    return math.sqrt(n)


def percentage(part, whole):
    return part / whole * 100
