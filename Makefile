
all: generate clean test

generate:
	python tools/generate.py

test:
	nosetests --with-coverage --cover-package=fingerprints --cover-erase

clean:
	rm -rf dist build .eggs .mypy_cache
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
