# Generated by Django 2.0.1 on 2018-03-21 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('importer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Filter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_conditional', models.CharField(choices=[('c', 'Contains'), ('p', 'Prefix'), ('s', 'Sufix'), ('r', 'Regular expresion'), ('g', 'Greater than'), ('G', 'Greater or equal than'), ('L', 'Lower or equal than'), ('l', 'Lower than')], max_length=1)),
                ('conditional', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('negate_conditional', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ValuesToTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enable', models.IntegerField(default=1)),
                ('automatic', models.IntegerField()),
                ('raw_data_source', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='importer.RawDataSource')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Tag')),
            ],
        ),
        migrations.AddField(
            model_name='tag',
            name='values',
            field=models.ManyToManyField(related_name='tags', through='management.ValuesToTag', to='importer.RawDataSource'),
        ),
        migrations.AddField(
            model_name='filter',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='filters', to='management.Tag'),
        ),
    ]