.PHONY: docs


install:
	pip install -e .[test,codegen]

generate:
	python -mcodegen

test:
	pytest tests/

mypy:
	 mypy --config-file=mypy.ini src/commercetools

coverage:
	pytest --cov=commercetools

runserver:
	python -mcommercetools.testing.server

format:
	black src/ tests/
	isort --recursive src tests

release:
	pip install twine wheel
	rm -rf build/* dist/*
	python setup.py sdist bdist_wheel
	twine upload dist/*

docs:
	make -C docs html
