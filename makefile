FLASK_APP = wsgi.py

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
