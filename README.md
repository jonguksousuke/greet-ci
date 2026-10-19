# greet-ci

GitHub Actions CI practice: a small greeting program tested, checked, and built on every push and pull request to `main`.

## Setup

Requires [uv](https://docs.astral.sh/uv/) (CI uses 0.8.14) and Python 3.11 or newer.

```bash
uv lock
```

## Run

```bash
uv run --locked python greet.py Hee   # Hello, Hee!
uv run --locked python greet.py       # Hello, world!
```

## Checks

```bash
uv run --locked pytest -q greet.py
uv run --locked black --check greet.py
uv run --locked flake8 greet.py
uv run --locked mypy greet.py
uv build
```
