import environ
import posixpath
import requests
from typing import Dict, List

env = environ.Env()
environ.Env.read_env("pokedex/pokedex/.env")

# A set of constants that might be useful to HTTP clients
DB_HOST = env('DATABASE_HOST')
TRAINER_PREFIX = "trainers"
POKEMON_PREFIX = "pokemon"
POKEMON_INFO_PREFIX = "pokemon_info"
POKEMON_TYPE_PREFIX = "pokemon_type"
MOVE_PREFIX = "moves"
CREATE = "create"
SERIES = "series"
TEAMS = "teams"
ASSOCIATE = "associate"


def format_path(base: str, components: List[str]) -> str:
    """
    Formats a base and http components with the HTTP protocol and the expected port.
    """
    url = "http://{}:8000/".format(base)

    for component in components:
        url = posixpath.join(url, component)
    return url + "/" if url[-1] != "/" else url
    
def assert_successful_create(url: str, payload: Dict[str, str]):
    """Assert that the create POST request was successful, otherwise raise an Error"""
    response = requests.post(url, json=payload)
    if response.status_code != 200:
        raise ValueError("Could not create test data, error code: {}\npayload data: {}".format(response.status_code, payload))