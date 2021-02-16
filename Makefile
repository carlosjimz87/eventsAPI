.PHONY: setup
setup:
	poetry install

.PHONY: build-requirements
build-requirements:
	poetry export -f requirements.txt --without-hashes > requirements.txt

.PHONY: run
run:
	python main.py


.PHONY: test
test:
	pytest