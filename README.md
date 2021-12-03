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
- You'll need to clean up your existing `pokedex` schema if you have one in your MySQL server. Drop all of the tables in your schema.
- Since Django is managing the database, you'll need to run `python3 manage.py migrate` in `pokedex/` to migrate all existing changes to the database. This will give you a fresh `pokedex` database managed by Django. If you do not already have a `pokedex` schema, create one and do not add any tables.
- Open up a terminal and run `make run` in the root directory
- To verify that the server is connected, visit the localhost page they provided in the output of your terminal, e.g. `http://127.0.0.1:8000/`

If you're connecting via WSL and need to connect to the host, you'll need to grant access for a MySQL user to connect to the server. You can follow [this](https://stackoverflow.com/a/1559992) link to set up the privileges, but be sure to adjust the user's IP following [this](https://stackoverflow.com/a/8348560).

- Once you verify that the initial set-up for the backend works, you can just run `make run` in the project directory to start the server whenever you want to. Be sure to leave this terminal in the background or daemonize the command in order to ensure that the server will continue running as you perform various operations on it.

## Trainer API
To access trainer data, you can use the `host:8000/trainers/` HTTP endpoint.

- Getting all trainers: `host:8000/trainers/`
- Getting a trainer by id: `host:8000/trainers/<id:int>/`
- Updating a trainer: `host:8000/trainers/update/<id:int>/`
- Creating a trainer: `host:8000/trainers/create/`
- Deleting a trainer: `host:8000/trainers/delete/<id:int>/`

For updating or creating, be sure to provide a JSON object in the body of your request mapping the trainer's keys to its values.
Updating a trainer's fields only requires that you provide the fields you want to change, instead of all fields.

JSON payload example:
```json
{
    "first_name": "kevin",
    "last_name": "hui",
    "username": "khui",
    "password": "mypass",
    "email": "hui.k@husky.neu.edu",
    "date_of_birth": "1987-05-22T00:00:00Z"
}
```

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

JSON payload for creating a PokemonInfo example:
```json
{
    "national_num": 29,
    "name": "pikachu",
    "photo_url": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/025.png",
    "description": "Pikachu that can generate powerful electricity have cheek sacs that are extra soft and super stretchy.",
    "evolved_state_pkid": 25,
    "devolved_state_pkid": 26
}
```

An example of creating a series of PokemonInfo:
```
[
    {
        "national_num": 172,
        "name": "Pichu",
        "photo_url": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/172.png",
        "description": "Despite its small size, it can zap even adult humans. However, if it does so, it also surprises itself."
    },
    {
        "national_num": 25,
        "name": "Pikachu",
        "photo_url": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/025.png",
        "description": "Pikachu that can generate powerful electricity have cheek sacs that are extra soft and super stretchy."
    },
    {
        "national_num": 26,
        "name": "Raichu",
        "photo_url": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/026.png",
        "description": "Its long tail serves as a ground to protect itself from its own high-voltage power."
    }
]
```
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

JSON payload example:
```
{
    "name": "Scratch",
    "description": "A Normal-type attack. Sharp claws are used to inflict damage on the target.",
    "move_type": "physical",
    "element_type": "normal"
}
```

## Generating Authentic Pokemon Data
We query PokeAPI's interface in order to extract legitimate data about pokemon. To set up your server with legitimate pokemon information, run `make build` in another terminal while the server is running.

## Generating sample data for all tables
We provide another Makefile command, `make test-build`, which will provide fake information about trainers, pokemon, and other classes relevant to the database.

## Clearing the database
To clean up your database, simply run `make clean` in another terminal while the server is running.


# Authors
- Natalie Hsu
- Kevin Hui
- Amy Ying
