# Generated by Django 3.2.3 on 2021-08-13 22:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0008_alter_linktype_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_type_id',
            field=models.ForeignKey(db_column='book_type_id', on_delete=django.db.models.deletion.CASCADE, related_name='books', to='resources.booktype', verbose_name='Book Type'),
        ),
        migrations.AlterField(
            model_name='booktype',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='document_type_id',
            field=models.ForeignKey(db_column='document_type_id', on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='resources.documenttype', verbose_name='Document Type'),
        ),
        migrations.AlterField(
            model_name='documenttype',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
