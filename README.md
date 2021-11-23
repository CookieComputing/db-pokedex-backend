# db-pokedex-backend

Backend for CS 3200 - Database Design. Contains code for querying PokeAPI, as well as servicing requests to the MySQL database.

## Onboarding
- Create `pokedex/.env`. This file will be used for storing various configuration values you may need to start the server. Here's an example of a file:
```
DATABASE_USER=<yourDBuser>
DATABASE_PASSWORD=<yourDBpassword>
DATABASE_NAME=pokedex
DATABASE_HOST=<yourDBhost, e.g. localhost>
```
- Create a virtual environment to remove any dependencies your machine may have, i.e. `python3 -m venv env`
- Run `source env/bin/activate` in the main directory to enable your virtual environment
- Run `pip install requirements.txt` in the main directory to install python requirements

## Starting the backend server
- ensure you're in a virtual environment, `make run`

# Authors
- Natalie Hsu
- Kevin Hui
- Amy Ying