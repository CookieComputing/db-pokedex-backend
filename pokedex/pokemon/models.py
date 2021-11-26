"""
Models for pokemon related data
"""
from django.db import models

from django.utils.translation import gettext_lazy as _

class PokemonInfo(models.Model):
    national_num = models.IntegerField(primary_key=True)
    evolved_state_pkid = models.ForeignKey('self', models.SET_NULL, db_column='evolved_state_pkid', blank=True, null=True, related_name="evolved_state")
    devolved_state_pkid = models.ForeignKey('self', models.SET_NULL, db_column='devolved_state_pkid', blank=True, null=True, related_name="devolved_state")
    name = models.CharField(max_length=45)
    photo_url = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    class Meta:
        db_table = 'pokemon_info'

class ElementTypes(models.TextChoices):
    NORMAL = "normal", _("Normal")
    FIRE = "fire", _("Fire")
    WATER = "water", _("Water")
    ELECTRIC = "electric", _("Electric")
    GRASS = "grass", _("Grass")
    ICE = "ice", _("Ice")
    FIGHTING = "fighting", _("Fighting")
    POISON = "poison", _("Poison")
    GROUND = "ground", _("Ground")
    FLYING = "flying", _("Flying")
    PSYCHIC = "psychic", _("Psychic")
    BUG = "bug", _("Bug")
    ROCK = "rock", _("Rock")
    GHOST = "ghost", _("Ghost")
    DRAGON = "dragon", _("Dragon")
    DARK = "dark", _("Dark")
    STEEL = "steel", _("Steel")
    FAIRY = "fairy", _("Fairy")

    class Meta:
        db_table = 'element_types'

class MoveTypes(models.TextChoices):
    PHYSICAL = "physical", _("Physical")
    STATUS = "status", _("Status")
    SPECIAL = "special", _("Special")

    class Meta:
        db_table = 'move_types'

class Moves(models.Model):
    mid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=255)
    element_type = models.CharField(max_length=45, choices=ElementTypes.choices)
    move_type = models.CharField(max_length=45, choices=MoveTypes.choices)

    class Meta:
        db_table = 'moves'
