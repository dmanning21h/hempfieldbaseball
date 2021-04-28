# Generated by Django 3.1.6 on 2021-04-04 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('coach_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=15)),
                ('coach_link', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Coaches',
                'db_table': 'Coach',
                'ordering': ['last_name'],
            },
        ),
        migrations.CreateModel(
            name='CoachRole',
            fields=[
                ('coach_role_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'Coach Role',
                'verbose_name_plural': 'Coach Roles',
                'db_table': 'CoachRole',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Height',
            fields=[
                ('height_id', models.AutoField(primary_key=True, serialize=False)),
                ('height', models.PositiveSmallIntegerField(unique=True)),
            ],
            options={
                'db_table': 'Height',
                'ordering': ['height'],
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('player_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=15)),
                ('player_link', models.CharField(max_length=30, unique=True)),
                ('graduation_year', models.PositiveSmallIntegerField()),
                ('bats', models.CharField(choices=[('R', 'R'), ('L', 'L'), ('S', 'S')], default='R', max_length=1)),
                ('throws', models.CharField(choices=[('R', 'R'), ('L', 'L')], default='R', max_length=1)),
            ],
            options={
                'db_table': 'Player',
                'ordering': ['last_name'],
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('position_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('abbr', models.CharField(max_length=15, unique=True)),
            ],
            options={
                'db_table': 'Position',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('team_id', models.AutoField(primary_key=True, serialize=False)),
                ('year', models.PositiveSmallIntegerField(unique=True)),
            ],
            options={
                'db_table': 'Team',
                'ordering': ['-year'],
            },
        ),
        migrations.CreateModel(
            name='TeamPlayer',
            fields=[
                ('team_player_id', models.AutoField(primary_key=True, serialize=False)),
                ('weight', models.PositiveSmallIntegerField()),
                ('number', models.PositiveSmallIntegerField(default=0)),
                ('roster_photo', models.ImageField(blank=True, null=True, upload_to='player-portraits')),
                ('height', models.ForeignKey(db_column='height_id', on_delete=django.db.models.deletion.PROTECT, to='teammanagement.height', verbose_name='Height')),
                ('info', models.ForeignKey(db_column='player_id', on_delete=django.db.models.deletion.CASCADE, to='teammanagement.player', verbose_name='Player')),
                ('position', models.ForeignKey(db_column='position_id', on_delete=django.db.models.deletion.PROTECT, to='teammanagement.position', verbose_name='Position')),
                ('team', models.ForeignKey(db_column='team_id', on_delete=django.db.models.deletion.CASCADE, related_name='players', to='teammanagement.team', verbose_name='Team')),
            ],
            options={
                'verbose_name': 'Team Player',
                'verbose_name_plural': 'Team Players',
                'db_table': 'TeamPlayer',
                'ordering': ['number'],
            },
        ),
        migrations.CreateModel(
            name='TeamCoach',
            fields=[
                ('team_coach_id', models.AutoField(primary_key=True, serialize=False)),
                ('roster_photo', models.ImageField(blank=True, null=True, upload_to='coach-portraits')),
                ('info', models.ForeignKey(db_column='coach_id', on_delete=django.db.models.deletion.CASCADE, to='teammanagement.coach', verbose_name='Coach')),
                ('role', models.ForeignKey(db_column='coach_role_id', on_delete=django.db.models.deletion.PROTECT, to='teammanagement.coachrole', verbose_name='Coach Role')),
                ('team', models.ForeignKey(db_column='team_id', on_delete=django.db.models.deletion.CASCADE, related_name='coaches', to='teammanagement.team', verbose_name='Team')),
            ],
            options={
                'verbose_name': 'Team Coach',
                'verbose_name_plural': 'Team Coaches',
                'db_table': 'TeamCoach',
            },
        ),
    ]
