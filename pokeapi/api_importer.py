"""
A module that will import PokeAPI data into the pokedex's database. This
module contacts the backend server and uses the appropriate API calls to
import the data.
"""
from typing import Any, Dict, List
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
UPDATE = "update"
ASSOCIATE = "associate"
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

def migrate_pokemon_info() -> List[Dict[str, Any]]:
    """
    Migrates pokemon information into the MySQL database. Downloading pokemon information will also attempt to
    associate with any moves stored in the database.
    
    :raises: Error if there is any issue with importing pokemon information
    """
    logger.info("Importing pokemon info...")
    pokemon_info = api.get_all_pokemon_info()

    for pokemon in pokemon_info:
        response = requests.post(_format_path(DB_HOST, [POKEMON_PREFIX, POKEMON_INFO_PREFIX, CREATE]), json=pokemon)

        if response.status_code != 200:
            raise ValueError("Unexpected error when importing pokemon_info data, error code: {}".format(response.status_code))

    logger.info("pokemon info successfully imported")
    return pokemon_info

def migrate_evolution_chains(pokemon_list: List[Dict[str, Any]]) -> None:
    """
    Connects each pokemon with their new predecessors and successors from the provided evolution chain.

    :raises: Error if there's an issue connecting each of the Pokemon in the evolution chain
    """

    pokemon_list = [pokemon for pokemon in pokemon_list if 'evolution_chain' in pokemon]
    evolution_chain_set = set([pokemon['evolution_chain'] for pokemon in pokemon_list])
    logger.info("creating evolution chains")
    chains = []
    for evolution_chain in evolution_chain_set:
        chains.append(api.get_evolution_chain_data(evolution_chain))

    logger.info("evolution chains successfully establishing, migrating in database")

    for chain in chains:
        if len(chain) <= 1:
            continue

        for i in range(len(chain)):
            if i == 0:
                updated_pokemon = {
                    "national_num": chain[i],
                    "evolved_state_pkid": chain[i+1]
                }
            elif i == len(chain)-1:
                updated_pokemon = {
                    "national_num": chain[i],
                    "devolved_state_pkid": chain[i-1]
                }
            else:
                updated_pokemon = {
                    "national_num": chain[i],
                    "evolved_state_pkid": chain[i+1],
                    "devolved_state_pkid": chain[i-1]
                }
            response = requests.post(_format_path(DB_HOST, [POKEMON_PREFIX, POKEMON_INFO_PREFIX, UPDATE, str(chain[i])]), json=updated_pokemon)
            if response.status_code != 200:
                raise ValueError("Error when updating the evolution chain, status code: {}, pokemon national_num: {}".format(response.status_code, chain[i]))
    logger.info("evolution chains successfully imported")



def associate_pokemon_info_with_moves(pokemon_info: List[Dict[str, Any]]) -> None:
    """
    Associates the pokemon information in the database with all of the moves they are associated with.
    """
    
    def apply_move_assocs(pokemon: Dict[str, Any]) -> None:
        moves = pokemon['moves']
        # We put a hard limit on the amount of moves a pokemon can know
        # because otherwise we would get M * P entries! Given that M = ~800 and P = ~1000, that's a lot of entries
        for move in moves[:10]:
            move_assoc = {"pokemon_info": int(pokemon['national_num']), "move": move}

            response = requests.post(_format_path(DB_HOST, [POKEMON_PREFIX, POKEMON_INFO_PREFIX, MOVE_PREFIX, ASSOCIATE]), json=move_assoc)
            if response.status_code != 200:
                raise ValueError("Unexpected error when associate pokemon info with move data, error code: {}".format(response.status_code))
    for pokemon in pokemon_info:
        apply_move_assocs(pokemon)

def _format_path(base, components):
    url = "http://{}:8000/".format(base)

    for component in components:
        url = posixpath.join(url, component)
    return url + "/" if url[-1] != "/" else url