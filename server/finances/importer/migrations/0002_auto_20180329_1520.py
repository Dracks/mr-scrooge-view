# Generated by Django 2.0.1 on 2018-03-29 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('importer', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rawdatasource',
            options={'ordering': ('-date', '-date_value', 'movement_name')},
        ),
    ]