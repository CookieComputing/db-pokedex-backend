"""
A module that will import PokeAPI data into the pokedex's database. This
module contacts the backend server and uses the appropriate API calls to
import the data.
"""
from pokeapi import api

import environ
import requests
import posixpath

env = environ.Env()
environ.Env.read_env("pokedex/pokedex/.env")

DB_HOST = env('DATABASE_HOST')
POKEMON_PREFIX = "pokemon"
MOVE_PREFIX = "moves"
CREATE = "create"

def migrate_moves() -> None:
    """
    Migrates move information into the MySQL database.
    :raises: Error if there is any issue with importing move data
    """
    moves = api.get_all_moves()

    for move in moves:
        response = requests.post(_format_path(DB_HOST, [POKEMON_PREFIX, MOVE_PREFIX, CREATE]), json=move)

        if response.status_code != 200:
            raise ValueError("Unexpected error when importing move data, error code: {}".format(response.status_code))

def _format_path(base, components):
    url = "http://{}:8000/".format(base)

    for component in components:
        url = posixpath.join(url, component)
    return url + "/" if url[-1] != "/" else url