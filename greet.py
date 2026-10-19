"""Greeting program used for the Week07 GitHub Actions CI practice."""

import sys


def greet(name: str) -> str:
    """Return a greeting for ``name``."""
    return f"Hello, {name}!"


def main(argv: list[str]) -> None:
    """Print a greeting for the first argument, or for ``world``."""
    name = argv[1] if len(argv) > 1 else "world"
    print(greet(name))


def test_greet() -> None:
    assert greet("Hee") == "Hello, Hee!"


if __name__ == "__main__":
    main(sys.argv)
