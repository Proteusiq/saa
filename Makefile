.PHONY: install format lint typecheck test check build clean

install:
	uv sync

format:
	uv run ruff format .

lint:
	uv run ruff check --fix .

typecheck:
	uv run ty check

test:
	uv run pytest

check: format lint typecheck test

build:
	uv build

clean:
	rm -rf dist build *.egg-info .pytest_cache .ruff_cache .hypothesis
