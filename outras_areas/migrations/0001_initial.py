# Generated by Django 2.1.2 on 2018-10-11 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PermissoesOutrasAreas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'permissions': (('outrasareas_permissoes', 'Permissão Global de Outras Areas'),),
                'managed': False,
            },
        ),
    ]
