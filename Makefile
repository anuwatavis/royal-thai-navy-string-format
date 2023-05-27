.PHONY: clean test build publishpypi publishtestpypi

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

publishtestpypi:
	make clean
	make test
	make build
	twine check dist/*  
	twine upload -r testpypi dist/*

publishpypi:
	make clean
	make test
	make build
	twine check dist/*  
	twine upload dist/*
	