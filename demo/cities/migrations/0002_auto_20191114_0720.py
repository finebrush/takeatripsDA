# Generated by Django 2.2.7 on 2019-11-13 22:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('cities', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='InfoTravelnew',
            new_name='InfoTravel',
        ),
    ]
