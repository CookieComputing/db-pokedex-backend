"""
Models for pokemon related data
"""
from django.db import models

class PokemonInfo(models.Model):
    national_num = models.IntegerField(primary_key=True)
    evolved_state_pkid = models.ForeignKey('self', models.SET_NULL, db_column='evolved_state_pkid', blank=True, null=True, related_name="evolved_state")
    devolved_state_pkid = models.ForeignKey('self', models.SET_NULL, db_column='devolved_state_pkid', blank=True, null=True, related_name="devolved_state")
    name = models.CharField(max_length=45)
    photo_url = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    class Meta:
        db_table = 'pokemon_info'