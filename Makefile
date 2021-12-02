.PHONY: run
run:
	python3 pokedex/manage.py runserver

.PHONY: build
build:
	echo "stub"

.PHONY: clean
clean:
	echo "stub"

.PHONY: test-build
test-build:
	python3 scripts/populate_test_data.py