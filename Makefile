.PHONY: setup freeze install run

# source : https://stackoverflow.com/questions/10858261/abort-makefile-if-variable-not-set
check_defined = \
    $(strip $(foreach 1,$1, \
        $(call __check_defined,$1,$(strip $(value 2)))))
__check_defined = \
    $(if $(value $1),, \
      $(error Undefined $1$(if $2, ($2))))

setup:
	python3.7 -m venv venv

freeze:
	$(call check_defined, VIRTUAL_ENV, please use a virtual environment)
	pip freeze > requirements.txt

install:
	$(call check_defined, VIRTUAL_ENV, please use a virtual environment)
	pip install -r requirements.txt

test: install
	pytest -vv

extract.german.nouns.from.file: install
	$(call check_defined, FIRST_CHARACTER, first character of the extracted nouns)
	$(call check_defined, SOURCE_FILE, path of the text file)
	python -m application.extract_german_nouns.run $(FIRST_CHARACTER) $(SOURCE_FILE)
