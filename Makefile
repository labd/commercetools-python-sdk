.PHONY: docs


install:
	uv sync --all-groups

generate:
	java -jar ../rmf-codegen/rmf-codegen.jar generate ../commercetools-api-reference/api-specs/api/api.raml -o src/commercetools/platform/ -t PYTHON_CLIENT
	java -jar ../rmf-codegen/rmf-codegen.jar generate ../commercetools-api-reference/api-specs/importapi/api.raml -o src/commercetools/importapi/ -t PYTHON_CLIENT
	java -jar ../rmf-codegen/rmf-codegen.jar generate ../commercetools-api-reference/api-specs/frontend-api/api.raml -o src/commercetools/frontend/ -t PYTHON_CLIENT
	java -jar ../rmf-codegen/rmf-codegen.jar generate ../commercetools-api-reference/api-specs/checkout/api.raml -o src/commercetools/checkout/ -t PYTHON_CLIENT
	find src/ -name "gen.properties" -delete
	uv run ruff check --fix --select I src/commercetools/
	uv run ruff format src/commercetools/

test:
	uv run pytest tests/

mypy:
	uv run mypy --config-file=mypy.ini src/commercetools

coverage:
	uv run pytest --cov=commercetools

runserver:
	uv run python -mcommercetools.testing.server

format:
	uv run ruff check --fix src tests
	uv run ruff format src tests

lint:
	uv run ruff format --check src tests
	uv run ruff check src tests

docs:
	uv run --group docs make -C docs html
