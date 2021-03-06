# Generated by Django 3.2.3 on 2021-08-13 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('playerresources', '0005_auto_20210813_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlelink',
            name='link_type_id',
            field=models.ForeignKey(db_column='link_type_id', on_delete=django.db.models.deletion.PROTECT, related_name='article_links', to='playerresources.linktype', verbose_name='Link Type'),
        ),
    ]
