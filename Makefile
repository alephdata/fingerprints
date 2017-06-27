
all: clean build test

build:
	python fetch.py

test:
	python test.py

upload:
	python setup.py sdist bdist_wheel upload -r pypi

clean:
	rm -rf dist build
