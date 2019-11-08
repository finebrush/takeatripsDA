# Generated by Django 2.2.4 on 2019-09-11 02:19

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0003_delete_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewMultiPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('nmp', django.contrib.gis.db.models.fields.MultiPointField(srid=4326)),
            ],
            options={
                'verbose_name': 'NewMultiPoint',
                'verbose_name_plural': 'NewMultiPoint',
                'db_table': 'newmultipoint',
            },
        ),
    ]
