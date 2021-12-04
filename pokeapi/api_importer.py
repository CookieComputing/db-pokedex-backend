"""
A module that will import PokeAPI data into the pokedex's database. This
module contacts the backend server and uses the appropriate API calls to
import the data.
"""
from pokeapi import api

import environ
import requests
import posixpath
import logging

env = environ.Env()
environ.Env.read_env("pokedex/pokedex/.env")

DB_HOST = env('DATABASE_HOST')
POKEMON_PREFIX = "pokemon"
MOVE_PREFIX = "moves"
POKEMON_INFO_PREFIX = "pokemon_info"
CREATE = "create"
logger = logging.getLogger("api_importer")
def migrate_moves() -> None:
    """
    Migrates move information into the MySQL database.
    :raises: Error if there is any issue with importing move data
    """
    logger.info("Importing moves...")
    moves = api.get_all_moves()

    for move in moves:
        response = requests.post(_format_path(DB_HOST, [POKEMON_PREFIX, MOVE_PREFIX, CREATE]), json=move)

        if response.status_code != 200:
            raise ValueError("Unexpected error when importing move data, error code: {}".format(response.status_code))
    logger.info("moves successfully imported")

def migrate_pokemon_info() -> None:
    """
    Migrates pokemon information into the MySQL database.
    
    :raises: Error if there is any issue with importing pokemon information
    """
    logger.info("Importing pokemon info...")
    pokemon_info = api.get_all_pokemon_info()

    for pokemon in pokemon_info:
        response = requests.post(_format_path(DB_HOST, [POKEMON_PREFIX, POKEMON_INFO_PREFIX, CREATE]), json=pokemon)

        if response.status_code != 200:
            raise ValueError("Unexpected error when importing move data, error code: {}".format(response.status_code))
    logger.info("pokemon info successfully imported")

def _format_path(base, components):
    url = "http://{}:8000/".format(base)

    for component in components:
        url = posixpath.join(url, component)
    return url + "/" if url[-1] != "/" else url