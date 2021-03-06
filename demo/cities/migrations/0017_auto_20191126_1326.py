# Generated by Django 2.2.7 on 2019-11-26 04:26

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0016_auto_20191126_1008'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newmultipoint',
            options={'verbose_name': '다중 Point', 'verbose_name_plural': '다중 Point'},
        ),
        migrations.AlterModelOptions(
            name='poipoint',
            options={'verbose_name': '여행코스', 'verbose_name_plural': '여행코스'},
        ),
        migrations.AddField(
            model_name='newmultipoint',
            name='travelplan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cities.TravelPlan', verbose_name='TravelPlan'),
        ),
        migrations.AlterField(
            model_name='poipoint',
            name='point',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326, verbose_name='위치'),
        ),
        migrations.AlterField(
            model_name='travelplan',
            name='courseinfoeng',
            field=models.TextField(blank=True, help_text='코스를 소개해 주세요.', null=True, verbose_name='코스정보(영어)'),
        ),
        migrations.AlterField(
            model_name='travelplan',
            name='courseinfoven',
            field=models.TextField(blank=True, help_text='코스를 소개해 주세요.', null=True, verbose_name='코스정보(베트남어)'),
        ),
    ]
