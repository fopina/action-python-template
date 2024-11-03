lint:
	ruff format
	ruff check --fix

lint-check:
	ruff format --diff
	ruff check

test:
	python -m pytest --cov
