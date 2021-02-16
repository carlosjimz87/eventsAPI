.PHONY: install-poetry
install-poetry:
ifeq ("$(wildcard ${HOME}/.poetry/env)", "")
	@echo "Poetry is not installed. Installing ..."
	curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3
else
	@echo "Poetry is already installed"
endif
	. ${HOME}/.poetry/env

.PHONY: setup
setup:
	poetry config virtualenvs.in-project true
	poetry install

fmt:
	poetry run isort api/
	poetry run black --target-version py36 --verbose api/
	poetry run flake8 api/
	poetry run isort models/
	poetry run black --target-version py36 --verbose models/
	poetry run flake8 models/
	poetry run isort providers/
	poetry run black --target-version py36 --verbose providers/
	poetry run flake8 providers/
	poetry run isort tests/
	poetry run black --target-version py36 --verbose tests/
	poetry run flake8 tests/
	poetry run isort utils/
	poetry run black --target-version py36 --verbose utils/
	poetry run flake8 utils/

.PHONY: build-requirements
build-requirements:
	poetry export -f requirements.txt --without-hashes > requirements.txt

.PHONY: test
test:
	pytest

.PHONY: run
run: install-poetry setup
	poetry run uvicorn main:app --reload
