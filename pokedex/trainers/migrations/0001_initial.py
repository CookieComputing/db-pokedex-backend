# Generated by Django 3.2.9 on 2021-11-24 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trainers',
            fields=[
                ('tid', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('username', models.CharField(max_length=45)),
                ('password', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=45)),
                ('date_of_birth', models.DateTimeField()),
            ],
            options={
                'db_table': 'trainers',
                'managed': False,
            },
        ),
    ]
