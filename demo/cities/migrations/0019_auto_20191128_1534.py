# Generated by Django 2.2.7 on 2019-11-28 06:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0006_auto_20191121_1825'),
        ('cities', '0018_auto_20191128_1517'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='infotravel',
            name='category',
        ),
        migrations.AddField(
            model_name='infotravel',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='common.CSmall'),
        ),
    ]
