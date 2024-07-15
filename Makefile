.PHONY: install
install:
	@poetry install
	@poetry run mypy --install-types


.PHONY: check
check:
	@poetry check --lock
	@poetry run ruff format
	@poetry run mypy