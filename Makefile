.PHONY: install
install:
	@poetry install
	@poetry run mypy --install-types


.PHONY: check
check:
	@poetry check --lock
	@poetry run ruff check --fix
	@poetry run ruff format
	@poetry run mypy


.PHONY: test
test:
	poetry run pytest
