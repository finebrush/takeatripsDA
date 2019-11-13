# Generated by Django 2.2.7 on 2019-11-13 22:17

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Name')),
                ('titleko', models.CharField(max_length=128, verbose_name='소개타이틀(한국어)')),
                ('titleeng', models.CharField(max_length=128, verbose_name='소개타이틀(영어)')),
                ('titleven', models.CharField(max_length=128, verbose_name='소개타이틀(베트남어)')),
                ('created', models.DateField(verbose_name='Created')),
                ('picture1', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Picture1')),
                ('picture2', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Picture2')),
                ('picture3', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Picture3')),
                ('picture4', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Picture4')),
                ('location', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326, verbose_name='Rocation')),
            ],
            options={
                'verbose_name': 'City',
                'verbose_name_plural': 'Cities',
                'db_table': 'city',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='InfoBasic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='UUID number')),
                ('ibname', models.CharField(max_length=64, verbose_name='Name')),
                ('ibrepicture', models.ImageField(upload_to='', verbose_name='Re-Picture')),
                ('ibtitle', models.CharField(max_length=128, verbose_name='Title')),
                ('ibwritter', models.CharField(max_length=64, verbose_name='Writter')),
                ('img1', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Image1')),
                ('img2', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Image2')),
                ('img3', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Image3')),
                ('img4', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Image4')),
                ('img5', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Image5')),
            ],
            options={
                'verbose_name': 'InfoBasic',
                'verbose_name_plural': 'InfoBasics',
                'db_table': 'infobasic',
            },
        ),
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
        migrations.CreateModel(
            name='SecondTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Name')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='Slug')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ThirdTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Name')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='Slug')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TravelCurator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tctitle', models.CharField(max_length=64, verbose_name='Title')),
                ('tcwritter', models.CharField(max_length=64, verbose_name='Writter')),
                ('ittag', models.CharField(max_length=64, verbose_name='Tag')),
                ('tcwritedate', models.DateField(verbose_name='Write Date')),
            ],
            options={
                'verbose_name': 'TravelCurator',
                'verbose_name_plural': 'TravelCurators',
                'db_table': 'travelcurator',
            },
        ),
        migrations.CreateModel(
            name='TravelPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tpname', models.CharField(max_length=40, verbose_name='Name')),
                ('tpcomment', models.CharField(max_length=64, verbose_name='Comment')),
            ],
            options={
                'verbose_name': 'TravelPlan',
                'verbose_name_plural': 'TravelPlan',
                'db_table': 'travelplan',
            },
        ),
        migrations.CreateModel(
            name='ThirdTaggedItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.IntegerField(db_index=True, verbose_name='Object id')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cities_thirdtaggeditem_tagged_items', to='contenttypes.ContentType', verbose_name='Content type')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cities_thirdtaggeditem_items', to='cities.ThirdTag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TCImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tcimgtitle', models.CharField(max_length=64, verbose_name='Image Title')),
                ('tcimg', models.ImageField(upload_to='', verbose_name='Trave Image')),
                ('travelcurator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cities.TravelCurator', verbose_name='TravelCurator')),
            ],
            options={
                'verbose_name': 'TCImage',
                'verbose_name_plural': 'TCImages',
                'db_table': 'tcimage',
            },
        ),
        migrations.CreateModel(
            name='SecondTaggedItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.IntegerField(db_index=True, verbose_name='Object id')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cities_secondtaggeditem_tagged_items', to='contenttypes.ContentType', verbose_name='Content type')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cities_secondtaggeditem_items', to='cities.SecondTag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='POIpoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=40, verbose_name='Name')),
                ('point', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326, verbose_name='Point')),
                ('travelplan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cities.TravelPlan', verbose_name='TravelPlan')),
            ],
            options={
                'verbose_name': 'POIpoint',
                'verbose_name_plural': 'POIpoint',
                'db_table': 'poipoint',
            },
        ),
        migrations.CreateModel(
            name='InfoTravelnew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyko', models.CharField(max_length=64, verbose_name='업체명(한국어)')),
                ('companyeng', models.CharField(max_length=64, verbose_name='업체명(영어)')),
                ('companyven', models.CharField(max_length=64, verbose_name='업체명(베트남어)')),
                ('picture1', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Picture2')),
                ('picture2', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Picture2')),
                ('picture3', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Picture2')),
                ('picture4', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Picture2')),
                ('part', models.CharField(choices=[(1, '먹다/마시다'), (2, '보다'), (3, '자다'), (4, '사다')], max_length=8, verbose_name='구분')),
                ('type', models.CharField(choices=[(1, 'Must See'), (2, 'Hot')], max_length=8, verbose_name='유형선택')),
                ('addressko', models.CharField(max_length=128, verbose_name='주소(한국어)')),
                ('addresseng', models.CharField(max_length=128, verbose_name='주소(영어)')),
                ('addressven', models.CharField(max_length=128, verbose_name='주소(베트남어)')),
                ('category', models.CharField(choices=[(1, 'Place'), (2, '랜드마크'), (3, '자연'), (4, '공원'), (5, '박물관'), (6, '종교'), (7, '거\x1f리'), (8, '시장'), (9, '교통'), (10, '공공')], max_length=8, verbose_name='카테고리')),
                ('linkweb', models.CharField(blank=True, max_length=64, null=True, verbose_name='외부링크(웹사이트)')),
                ('linkinsta', models.CharField(blank=True, max_length=64, null=True, verbose_name='외부링크(인스타그램)')),
                ('linkyoutube', models.CharField(blank=True, max_length=64, null=True, verbose_name='외부링크(유튜브)')),
                ('trafficko', models.CharField(blank=True, max_length=128, null=True, verbose_name='교통정보(한국어)')),
                ('trafficeng', models.CharField(blank=True, max_length=128, null=True, verbose_name='교통정보(영어)')),
                ('trafficven', models.CharField(blank=True, max_length=128, null=True, verbose_name='교통정보(베트남어)')),
                ('introko', models.TextField(blank=True, help_text='이곳을 소개해 주세요.', null=True, verbose_name='소개정보(한국어)')),
                ('introeng', models.TextField(blank=True, help_text='이곳을 소개해 주세요.', null=True, verbose_name='소개정보(영어)')),
                ('introven', models.TextField(blank=True, help_text='이곳을 소개해 주세요.', null=True, verbose_name='소개정보(베트남어)')),
                ('itdate', models.DateField(verbose_name='Date')),
                ('itlocation', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326, verbose_name='Rocation')),
                ('tageng', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='cities.SecondTaggedItem', to='cities.SecondTag', verbose_name='태그(영어)')),
                ('tagko', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='태그(한국어)')),
                ('tagven', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='cities.ThirdTaggedItem', to='cities.ThirdTag', verbose_name='태그(베트남어)')),
            ],
            options={
                'verbose_name': 'InfoTravel',
                'verbose_name_plural': 'InfoTravels',
                'db_table': 'infotravel',
            },
        ),
    ]
