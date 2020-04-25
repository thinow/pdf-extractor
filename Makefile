.PHONY: setup freeze install

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

extract.german.nouns.from.file:
	$(call check_defined, FIRST_CHARACTER, first character of the extracted nouns)
	$(call check_defined, SOURCE_FILE, path of the text file)
	python -m application.extract_german_nouns.run_single_file $(FIRST_CHARACTER) $(SOURCE_FILE)

extract.german.nouns.from.directory:
	$(call check_defined, SOURCE_DIRECTORY, path of the directory containing the source files)
	python -m application.extract_german_nouns.run_directory $(SOURCE_DIRECTORY)

clean.extracted.nouns:
	$(call check_defined, SOURCE_FILE, path of the extracted nouns file)
	python -m application.clean_extracted_nouns.run $(SOURCE_FILE)
