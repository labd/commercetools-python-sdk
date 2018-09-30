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

release:
	pip install twine wheel
	rm -rf build/* dist/*
	python setup.py sdist bdist_wheel
	twine upload dist/*
