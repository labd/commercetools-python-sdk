.PHONY: docs


install:
	pip install -e .[test]

generate:
	java -jar ../rmf-codegen/rmf-codegen.jar generate ../commercetools-api-reference/api-specs/api/api.raml -o src/commercetools/platform/ -t PYTHON_CLIENT
	java -jar ../rmf-codegen/rmf-codegen.jar generate ../commercetools-api-reference/api-specs/importapi/api.raml -o src/commercetools/importapi/ -t PYTHON_CLIENT
	java -jar ../rmf-codegen/rmf-codegen.jar generate ../commercetools-api-reference/api-specs/frontend-api/api.raml -o src/commercetools/frontend/ -t PYTHON_CLIENT
	java -jar ../rmf-codegen/rmf-codegen.jar generate ../commercetools-api-reference/api-specs/checkout/api.raml -o src/commercetools/checkout/ -t PYTHON_CLIENT
	find src/ -name "gen.properties" -delete
	ruff check --fix --select I src/commercetools/
	ruff format src/commercetools/

test:
	pytest tests/

mypy:
	 mypy --config-file=mypy.ini src/commercetools

coverage:
	pytest --cov=commercetools

runserver:
	python -mcommercetools.testing.server

format:
	ruff check --fix src tests
	ruff format src tests

lint:
	ruff format --check src tests
	ruff check src tests

release:
	pip install twine wheel
	rm -rf build/* dist/*
	python setup.py sdist bdist_wheel
	twine upload dist/*

docs:
	make -C docs html
