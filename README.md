# db-pokedex-backend

Backend for CS 3200 - Database Design. Contains code for querying PokeAPI, as well as servicing requests to the MySQL database.

## Onboarding

- You'll need to ensure `python3` is installed on your systems. If you're on MacOS, the command is `brew install python`. If you're on some *nix system, the command is probably `sudo apt-get install python3`
- Create `pokedex/pokedex/.env`. This file will be used for storing various configuration values you may need to start the server. Here's an example of a file:
```
DATABASE_USER=<yourDBuser, e.g. root>
DATABASE_PASSWORD=<yourDBpassword, e.g. pass>
DATABASE_NAME=pokedex
DATABASE_HOST=<yourDBhost, e.g. localhost>
```
- Create a virtual environment to remove any dependencies your machine may have, i.e. `python3 -m venv env`
- Run `source env/bin/activate` in the main directory to enable your virtual environment
- Run `pip install -r requirements.txt` in the main directory to install python requirements
- You may end up encountering a few build errors thanks to missing dependencies, feel free to look them up on the internet to debug the build process

## Starting the backend server
- Ensure you're in the virtual environment with the requirements already installed
- You'll need to clean up your existing `pokedex` table if you have one in your MySQL server. Drop all of the tables in your schema.
- Since Django is managing the database, you'll need to run `python3 manage.py migrate` to migrate all existing changes to the database. This will give you a fresh `pokedex` database managed by Django.
- Open up a terminal and run `make run` in the root directory
- To verify that the server is connected, visit the localhost page they provided in the output of your terminal, e.g. `http://127.0.0.1:8000/`

If you're connecting via WSL and need to connect to the host, you'll need to grant access for a MySQL user to connect to the server. You can follow [this](https://stackoverflow.com/a/1559992) link to set up the privileges, but be sure to adjust the user's IP following [this](https://stackoverflow.com/a/8348560).

## Trainer API
To access trainer data, you can use the `host:8000/trainers/` HTTP endpoint.

- Getting all trainers: `host:8000/trainers/`
- Getting a trainer by id: `host:8000/trainers/<id:int>/`
- Updating a trainer: `host:8000/trainers/update/<id:int>/`
- Creating a trainer: `host:8000/trainers/create/`
- Deleting a trainer: `host:8000/trainers/delete/<id:int>/`

For updating or creating, be sure to provide a JSON object mapping the trainer's keys to its values.
Updating a trainer's fields only requires that you provide the fields you want to change, instead of all fields.

Make sure your datetime payload follows the `'%Y-%m-%dT%H:%M:%SZ'` format, otherwise the server will reject your payload.

## Pokemon Info API
Pokemon Info is an entry that contains the pokedex information about a specific pokemon species. To access this information, you can use
the `host:8000/pokemon/pokemon_info/` HTTP endpoint.

- Getting all pokemon info: `host:8000/pokemon/pokemon_info/`
- Getting pokemon info by id: `host:8000/pokemon/pokemon_info/<id:int>/`
- Updating pokemon info: `host:8000/pokemon/pokemon_info/update/<id:int>/`
- Deleting pokemon info: `host:8000/pokemon/pokemon_info/delete/<id:int>/`
- Creating pokemon info entries: `host:8000/pokemon/pokemon_info/create/`
- Creating a series of evoluions of pokemon: `host:8000/pokemon/pokemon_info/create/series/`

For updating or creating, be sure to provide a JSON object mapping the pokemon info's keys to its values.
Updating a pokemon info's fields only requires that you provide the fields you want to change, instead of all fields.

When creating a series of pokemon in an evolution chain, supply the attributes of each entry in a JSON array, where
the first entry is the most basic stage of the pokemon, and the last entry is the most evolved stage of the pokemon.

## Move API
Moves are the moves that a pokemon can use in battle. To access this information, you can use the 
`host:8000/pokemon/move` HTTP endpoint.

- Getting all moves: `host:8000/pokemon/moves/`
- Getting a move by id: `host:8000/pokemon/moves/<id:int>/`
- Updating a move: `host:8000/pokemon/moves/update/<id:int>/`
- Deleting a move: `host:8000/pokemon/moves/delete/<id:int>/`
- Creating a move: `host:8000/pokemon/moves/create/`

For updating or creating, be sure to provide a JSON object mapping the move's keys to its values.
Updating a move's fields only requires that you provide the fields you want to change, instead of all fields.

# Authors
- Natalie Hsu
- Kevin Hui
- Amy Ying
