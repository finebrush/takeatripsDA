# Generated by Django 2.2.7 on 2019-11-15 00:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0002_infotravel_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='infotravel',
            name='test',
        ),
    ]