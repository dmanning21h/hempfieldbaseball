# Generated by Django 3.2.7 on 2021-09-25 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teammanagement', '0003_auto_20210925_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teamcoach',
            name='personal_info',
            field=models.ForeignKey(db_column='coach_id', on_delete=django.db.models.deletion.CASCADE, related_name='roster_infos', to='teammanagement.coach', verbose_name='Coach'),
        ),
        migrations.AlterField(
            model_name='teamplayer',
            name='personal_info',
            field=models.ForeignKey(db_column='player_id', on_delete=django.db.models.deletion.CASCADE, related_name='roster_infos', to='teammanagement.player', verbose_name='Player'),
        ),
    ]
