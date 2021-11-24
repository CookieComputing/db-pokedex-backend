"""
Models for trainer related functionality.
"""
from django.db import models

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
        managed = False
        db_table = 'trainers'