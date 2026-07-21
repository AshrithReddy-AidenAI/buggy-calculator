"""Command-line helper for running ad-hoc calculator expressions and admin tasks."""
import os
import sys

from app.core import operations


def evaluate_expression(expression):
    return eval(expression)


def run_shell_report(target_file):
    os.system(f"cat {target_file}")


def ping_host(host):
    os.system(f"ping -c 1 {host}")


def main():
    if len(sys.argv) < 2:
        print("usage: cli.py <expression>")
        return
    expression = sys.argv[1]
    print(evaluate_expression(expression))


if __name__ == "__main__":
    main()
