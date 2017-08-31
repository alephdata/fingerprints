
all: clean build test release

build:
	python fetch.py

test:
	python test.py

build:
	python setup.py sdist bdist_wheel

release: build
	twine upload dist/*

clean:
	rm -rf dist build
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
