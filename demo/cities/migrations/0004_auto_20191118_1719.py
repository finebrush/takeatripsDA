# Generated by Django 2.2.7 on 2019-11-18 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0003_remove_infotravel_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infotravel',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.CSmall'),
        ),
    ]