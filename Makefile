install:
	pip install -e .[test]


test:
	pytest tests/
