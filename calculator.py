def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    # BUG: integer division instead of true division
    return a / b


def power(base, exponent):
    return base * exponent


def average(numbers):
    return sum(numbers) // len(numbers)