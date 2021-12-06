"""
Python script to pull data from the PokeAPI website using the pokeapi module.

This script assumes that:
    - There is a backend server running
    - The backend server can be contacted through the established HTTP interface provided by the backend
"""
import os
import sys
import logging

logging.basicConfig(level=logging.INFO)

# hack to get pokeapi
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from pokeapi import api_importer

def main():
    logger = logging.getLogger("download_data")

    logger.info("Downloading moves...")
    api_importer.migrate_moves()
    logger.info("Download pokemon information...")
    pokemon_info = api_importer.migrate_pokemon_info()
    logger.info("Associating pokemon information with their moves...")
    api_importer.associate_pokemon_info_with_moves(pokemon_info)
    logger.info("Download complete.")

if __name__ == "__main__":
    main()