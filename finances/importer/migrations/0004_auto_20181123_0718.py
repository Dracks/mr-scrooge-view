# Generated by Django 2.0.8 on 2018-11-23 07:18

from django.db import migrations


class Migration(migrations.Migration):

    # Don't pass the tests
    atomic = False

    dependencies = [
        ('importer', '0003_auto_20180920_1828'),
        ('management', '0003_auto_20180503_1926'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[
                migrations.AlterModelTable(
                    name='rawdatasource',
                    table='core_rawdatasource',
                ),
            ],
        ),
    ]
