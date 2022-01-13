FLASK_APP=wsgi.py

.PHONY: default
default: run

.PHONY: install
install:
	pip install -r requirements.txt

.PHONY: run
run:
	flask run

.PHONY: test
test:
	python -m unittest

.PHONY: load_test
load_test:
	# it's required to have the server running on the background to run
	# these tests
	cd tests; sh test_curl.sh
