.PHONY: setup
setup:
	poetry install

.PHONY: build-requirements
build-requirements:
	poetry export -f requirements.txt --without-hashes > requirements.txt

.PHONY: run
run:
	poetry run uvicorn main:app


.PHONY: test
test:
	pytest