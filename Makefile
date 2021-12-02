.PHONY: run
run:
	python3 pokedex/manage.py runserver

.PHONY: build
build:
	echo "stub"

.PHONY: clean
clean:
	python3 pokedex/manage.py flush 

.PHONY: test-build
test-build:
	echo "stub"