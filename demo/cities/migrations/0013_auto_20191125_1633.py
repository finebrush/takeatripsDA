# Generated by Django 2.2.7 on 2019-11-25 07:33

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('cities', '0012_auto_20191122_1353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='travelplan',
            name='tpcomment',
        ),
        migrations.RemoveField(
            model_name='travelplan',
            name='tpname',
        ),
        migrations.AddField(
            model_name='travelplan',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cities.City', verbose_name='City'),
        ),
        migrations.AddField(
            model_name='travelplan',
            name='course',
            field=models.IntegerField(choices=[(1, '1시간'), (2, '반나절'), (3, '하루')], default=1, verbose_name='코스선택'),
        ),
        migrations.AddField(
            model_name='travelplan',
            name='courseinfoeng',
            field=models.TextField(blank=True, help_text='코스를 소개해 주세요.', null=True, verbose_name='코스정보(한국어)'),
        ),
        migrations.AddField(
            model_name='travelplan',
            name='courseinfoko',
            field=models.TextField(blank=True, help_text='코스를 소개해 주세요.', null=True, verbose_name='코스정보(한국어)'),
        ),
        migrations.AddField(
            model_name='travelplan',
            name='courseinfoven',
            field=models.TextField(blank=True, help_text='코스를 소개해 주세요.', null=True, verbose_name='코스정보(한국어)'),
        ),
        migrations.AddField(
            model_name='travelplan',
            name='created',
            field=models.DateField(null=True, verbose_name='Created'),
        ),
        migrations.AddField(
            model_name='travelplan',
            name='tageng',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='cities.SecondTaggedItem', to='cities.SecondTag', verbose_name='태그(영어)'),
        ),
        migrations.AddField(
            model_name='travelplan',
            name='tagko',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='태그(한국어)'),
        ),
        migrations.AddField(
            model_name='travelplan',
            name='tagven',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='cities.ThirdTaggedItem', to='cities.ThirdTag', verbose_name='태그(베트남어)'),
        ),
        migrations.AddField(
            model_name='travelplan',
            name='titleeng',
            field=models.CharField(max_length=128, null=True, verbose_name='소개타이틀(영어)'),
        ),
        migrations.AddField(
            model_name='travelplan',
            name='titleko',
            field=models.CharField(max_length=128, null=True, verbose_name='소개타이틀(한국어)'),
        ),
        migrations.AddField(
            model_name='travelplan',
            name='titleven',
            field=models.CharField(max_length=128, null=True, verbose_name='소개타이틀(베트남어)'),
        ),
    ]
