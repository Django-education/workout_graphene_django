# Generated by Django 4.0 on 2021-12-22 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0002_rename_trainings_training'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Training',
            new_name='Workout',
        ),
    ]
