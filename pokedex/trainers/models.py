"""
Models for trainer related functionality.
"""
from datetime import datetime
from django.db import models
from pokemon.models import Gender, PokemonInfo, Region

class Trainers(models.Model):
    tid = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    date_of_birth = models.DateTimeField()

    def __str__():
        return "{} {}".format(self.first_name, self.last_name)
    
    class Meta:
        db_table = 'trainers'

class Teams(models.Model):
    name = models.CharField(max_length=45)
    trainer = models.ForeignKey(Trainers, models.CASCADE)

    def __str__():
        return "Trainer {} {}'s team {}".format(self.trainer.first_name, self.trainer.last_name, self.name)

    class Meta:
        db_table = 'teams'

class Pokemon(models.Model):
    """
    The pokemon that trainers own. This is distinct from the PokemonInfo, which contains information about
    the species in general
    """
    nickname = models.CharField(max_length=45)
    gender = models.CharField(max_length=45, choices=Gender.choices)
    team = models.ForeignKey(Teams, on_delete=models.CASCADE)
    pokemon_info = models.ForeignKey(PokemonInfo, on_delete=models.CASCADE)

    def __str__():
        return "{}".format(self.nickname)
    
    class Meta:
        db_table = "pokemon"
        
class Pokedex(models.Model):
    """
    The Pokedex contains a region and what PokemonInfos it contains.
    """
    region = models.CharField(max_length=45, choices=Region.choices)
    trainer = models.ForeignKey(Trainers, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "pokedex"
        unique_together = (('region', 'trainer'),)

class PokedexEntry(models.Model):
    """
    A reification of a many-to-many relationship between Pokedexes and PokemonInfo
    """
    pokedex = models.ForeignKey(Pokedex, on_delete=models.CASCADE)
    pokemon_info = models.ForeignKey(PokemonInfo, on_delete=models.CASCADE)

    class Meta:
        db_table = "pokedex_entry"
        # There should only be one entry for each pair in the database
        unique_together = (('pokedex', 'pokemon_info'),)
    