.PHONY: clean test build

clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type d -name ".pytest_cache" -exec rm -r {} +
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	rm -rf dist
	rm -rf build

test:
	python -m unittest

build:
	python setup.py bdist_wheel sdist     
