# Generated by Django 3.2.3 on 2021-05-22 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumniplayer',
            name='college_roster_link',
            field=models.URLField(max_length=75, unique=True),
        ),
    ]
