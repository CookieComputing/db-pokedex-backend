# Generated by Django 3.2.9 on 2021-12-12 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainers', '0006_pokedex'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokedex',
            old_name='type',
            new_name='region',
        ),
        migrations.AlterUniqueTogether(
            name='pokedex',
            unique_together={('region', 'trainer')},
        ),
    ]