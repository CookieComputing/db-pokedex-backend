.PHONY: run
run:
	python3 pokedex/manage.py runserver

.PHONY: build
build:
	python3 scripts/download_data.py

.PHONY: clean
clean:
	python3 pokedex/manage.py flush 

.PHONY: test-build
test-build:
	python3 scripts/populate_test_data.py