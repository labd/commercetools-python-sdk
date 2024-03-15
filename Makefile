.PHONY: docs


install:
	pip install -e .[test]

generate:
	java -jar ../rmf-codegen/rmf-codegen.jar generate ../commercetools-api-reference/api-specs/api/api.raml -o src/commercetools/platform/ -t PYTHON_CLIENT
	java -jar ../rmf-codegen/rmf-codegen.jar generate ../commercetools-api-reference/api-specs/importapi/api.raml -o src/commercetools/importapi/ -t PYTHON_CLIENT
	java -jar ../rmf-codegen/rmf-codegen.jar generate ../commercetools-api-reference/api-specs/frontend-api/api.raml -o src/commercetools/frontend/ -t PYTHON_CLIENT
	java -jar ../rmf-codegen/rmf-codegen.jar generate ../commercetools-api-reference/api-specs/checkout/api.raml -o src/commercetools/checkout/ -t PYTHON_CLIENT
	find src/ -name "gen.properties" -delete
	isort src/commercetools/
	black src/commercetools/

test:
	pytest tests/

mypy:
	 mypy --config-file=mypy.ini src/commercetools

coverage:
	pytest --cov=commercetools

runserver:
	python -mcommercetools.testing.server

format:
	isort src tests
	black src/ tests/

release:
	pip install twine wheel
	rm -rf build/* dist/*
	python setup.py sdist bdist_wheel
	twine upload dist/*

docs:
	make -C docs html
