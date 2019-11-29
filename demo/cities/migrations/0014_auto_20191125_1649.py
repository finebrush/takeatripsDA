# Generated by Django 2.2.7 on 2019-11-25 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0013_auto_20191125_1633'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poipoint',
            name='pname',
        ),
        migrations.AddField(
            model_name='poipoint',
            name='pnameeng',
            field=models.CharField(max_length=40, null=True, verbose_name='장소명(영어)'),
        ),
        migrations.AddField(
            model_name='poipoint',
            name='pnameko',
            field=models.CharField(max_length=40, null=True, verbose_name='장소명(한국어)'),
        ),
        migrations.AddField(
            model_name='poipoint',
            name='pnameven',
            field=models.CharField(max_length=40, null=True, verbose_name='장소명(베트남어)'),
        ),
        migrations.CreateModel(
            name='PointImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pimage', models.ImageField(blank=True, null=True, upload_to='', verbose_name='picture')),
                ('poipoint', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cities.POIpoint')),
            ],
        ),
    ]