# Generated by Django 2.2.7 on 2019-11-22 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0010_auto_20191121_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travelcurator',
            name='infotravel',
            field=models.ManyToManyField(to='cities.InfoTravel', verbose_name='여행장소'),
        ),
    ]
