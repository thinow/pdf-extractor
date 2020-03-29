.PHONY: setup lock install run prepare-build build

setup:
	python3.7 -m venv venv

freeze:
	$(call check_defined, VIRTUAL_ENV, please use a virtual environment)
	pip freeze > requirements.txt

install:
	$(call check_defined, VIRTUAL_ENV, please use a virtual environment)
	pip install -r requirements.txt

run: install
	python -m application.runner
