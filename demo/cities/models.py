from django.conf import settings
from django.db import models

from django.contrib.gis.db import models
from django.db.models import Manager as GeoManager
from django.contrib.gis.db import models as gismodels

from django.utils.translation import gettext_lazy as _

from demo.cities.choices import SELECT_PART, SELECT_TYPE, SELECT_CATEGORY
import uuid
from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase, CommonGenericTaggedItemBase, TagBase, GenericTaggedItemBase
from django.utils.html import format_html
from imagekit.models import ImageSpecField
from imagekit.processors import Thumbnail

class City(models.Model):
    name = models.CharField(_('Name'), max_length=64)
    titleko = models.CharField(_('소개타이틀(한국어)'), max_length=128)
    titleeng = models.CharField(_('소개타이틀(영어)'), max_length=128)
    titleven = models.CharField(_('소개타이틀(베트남어)'), max_length=128)
    created = models.DateField(_('Created'))
    picture1 = models.ImageField(_('Picture1'), null=True, blank=True)
    photo_thumbnail = ImageSpecField(
        source = 'picture1', 		   # 원본 ImageField 명
    	processors = [Thumbnail(100, 100)], # 처리할 작업목록
    	format = 'JPEG',		   # 최종 저장 포맷
    	options = {'quality': 60}
    ) # 저장 옵션

    def picture_tag(self):
        return format_html('<a href="{0}"><img src="{1}"></a>'.format(self.picture1.url, self.photo_thumbnail.url))
    picture_tag.allow_tags = True
    picture_tag.short_description = 'Image'

    picture2 = models.ImageField(_('Picture2'), null=True, blank=True)
    picture3 = models.ImageField(_('Picture3'), null=True, blank=True)
    picture4 = models.ImageField(_('Picture4'), null=True, blank=True)

    location = models.PointField(verbose_name='Rocation',srid = 4326, null=True, blank=True)
    objects = GeoManager()

    class Meta:
        verbose_name = _('City')
        verbose_name_plural = _('Cities')
        db_table = 'city'
        ordering = ('name',)

    def __str__(self):
        return self.name

class InfoBasic(models.Model):
    uuid = models.UUIDField(verbose_name=_('UUID number'), default=uuid.uuid4, editable=False)
    ibname = models.CharField(_('Name'), max_length=64)
    # city = models.ForeignKey(
    #     'cities.City', verbose_name=_('City'), on_delete=models.CASCADE, null=True, blank=True
    # )

    ibrepicture = models.ImageField(_('Re-Picture'), null=False, blank=False)
    photo_thumbnail = ImageSpecField(
        source = 'ibrepicture', 		   # 원본 ImageField 명
    	processors = [Thumbnail(100, 100)], # 처리할 작업목록
    	format = 'JPEG',		   # 최종 저장 포맷
    	options = {'quality': 60}
    ) # 저장 옵션

    def ibrepicture_tag(self):
        return format_html('<a href="{0}"><img src="{1}"></a>'.format(self.ibrepicture.url, self.photo_thumbnail.url))
    ibrepicture_tag.allow_tags = True
    ibrepicture_tag.short_description = 'Image'

    ibtitle = models.CharField(_('Title'), max_length=128)
    ibwritter = models.CharField(_('Writter'), max_length=64)
    img1 = models.ImageField(_('Image1'), null=True, blank=True)
    img2 = models.ImageField(_('Image2'), null=True, blank=True)
    img3 = models.ImageField(_('Image3'), null=True, blank=True)
    img4 = models.ImageField(_('Image4'), null=True, blank=True)
    img5 = models.ImageField(_('Image5'), null=True, blank=True)

    class Meta:
        verbose_name = _('InfoBasic')
        verbose_name_plural = _('InfoBasics')
        db_table = 'infobasic'


class SecondTag(TagBase):
    pass

class SecondTaggedItem(GenericTaggedItemBase):
    tag = models.ForeignKey(SecondTag, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_items",)

class ThirdTag(TagBase):
    pass

class ThirdTaggedItem(GenericTaggedItemBase):
    tag = models.ForeignKey(ThirdTag, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_items",)

class InfoTravel(models.Model):
    companyko = models.CharField(_('업체명(한국어)'), max_length=64)
    companyeng = models.CharField(_('업체명(영어)'), max_length=64)
    companyven = models.CharField(_('업체명(베트남어)'), max_length=64)
    picture1 = models.ImageField(_('Picture2'), null=True, blank=True)
    picture2 = models.ImageField(_('Picture2'), null=True, blank=True)
    picture3 = models.ImageField(_('Picture2'), null=True, blank=True)
    picture4 = models.ImageField(_('Picture2'), null=True, blank=True)
    part = models.CharField(_('구분'), choices=SELECT_PART, max_length=8)
    type = models.CharField(_('유형선택'), choices=SELECT_TYPE, max_length=8)
    addressko = models.CharField(_('주소(한국어)'), max_length=128)
    addresseng = models.CharField(_('주소(영어)'), max_length=128)
    addressven = models.CharField(_('주소(베트남어)'), max_length=128)
    category = models.CharField(_('카테고리'), choices=SELECT_CATEGORY, max_length=8)
    linkweb = models.CharField(_('외부링크(웹사이트)'), max_length=64, null=True, blank=True)
    linkinsta = models.CharField(_('외부링크(인스타그램)'), max_length=64, null=True, blank=True)
    linkyoutube = models.CharField(_('외부링크(유튜브)'), max_length=64, null=True, blank=True)
    trafficko = models.CharField(_('교통정보(한국어)'), max_length=128, null=True, blank=True)
    trafficeng = models.CharField(_('교통정보(영어)'), max_length=128, null=True, blank=True)
    trafficven = models.CharField(_('교통정보(베트남어)'), max_length=128, null=True, blank=True)
    introko = models.TextField(_('소개정보(한국어)'), null=True, blank=True, help_text=_('이곳을 소개해 주세요.'))
    introeng = models.TextField(_('소개정보(영어)'), null=True, blank=True, help_text=_('이곳을 소개해 주세요.'))
    introven = models.TextField(_('소개정보(베트남어)'), null=True, blank=True, help_text=_('이곳을 소개해 주세요.'))
    tagko = TaggableManager(_('태그(한국어)'))
    # tagko.related_name = "+"
    tageng = TaggableManager(_('태그(영어)'), through=SecondTaggedItem)
    # tageng.related_name = "+"
    tagven = TaggableManager(_('태그(베트남어)'), through=ThirdTaggedItem)
    # tagven.related_name = "+"
    
    # thumbnail 만들기..
    photo_thumbnail = ImageSpecField(
        source = 'picture1', 		   # 원본 ImageField 명
    	processors = [Thumbnail(100, 100)], # 처리할 작업목록
    	format = 'JPEG',		   # 최종 저장 포맷
    	options = {'quality': 60}
    ) # 저장 옵션
    # admin에 html 로 나타내기.. admin.py 에서 아래 태그를 list_display 한다..
    def picture_tag(self):
        return format_html('<a href="{0}"><img src="{1}"></a>'.format(self.picture1.url, self.photo_thumbnail.url))
    picture_tag.allow_tags = True
    picture_tag.short_description = 'Image'

    itdate = models.DateField(_('Date'))
    # 지도 위에서 POI 로 지정..
    itlocation = models.PointField(verbose_name='Rocation',srid = 4326, null=True, blank=True)
    objects = GeoManager()

    class Meta:
        verbose_name = _('InfoTravel')
        verbose_name_plural = _('InfoTravels')
        db_table = 'infotravel'

    def __str__(self):
        return self.companyko

class TravelCurator(models.Model):
    # tcname = models.CharField(_('Name'), max_length=64)
    # city = models.ForeignKey(
    #     'cities.City', verbose_name=_('City'), on_delete=models.CASCADE, null=True, blank=True
    # )
    tctitle = models.CharField(_('Title'), max_length=64)
    tcwritter = models.CharField(_('Writter'), max_length=64)
    ittag = models.CharField(_('Tag'), max_length=64)
    tcwritedate = models.DateField(_('Write Date'))
    # infotravel = models.ManyToManyField(
    #     'cities.InfoTravel', verbose_name=_('InfoTravels')
    # )

    class Meta:
        verbose_name = _('TravelCurator')
        verbose_name_plural = _('TravelCurators')
        db_table = 'travelcurator'

class TCImage(models.Model):
    travelcurator = models.ForeignKey(
        'cities.TravelCurator', verbose_name=_('TravelCurator'), on_delete=models.CASCADE, null=True, blank=True
    )
    tcimgtitle = models.CharField(_('Image Title'), max_length=64)
    tcimg = models.ImageField(_('Trave Image'), null=False, blank=False)

    class Meta:
        verbose_name = _('TCImage')
        verbose_name_plural = _('TCImages')
        db_table = 'tcimage'

class TravelPlan(models.Model):
    # city = models.ForeignKey(
    #     'cities.City', verbose_name=_('City'), on_delete=models.CASCADE, null=True, blank=True
    # )
    tpname = models.CharField(_('Name'), max_length=40)
    tpcomment = models.CharField(_('Comment') ,max_length=64)

    class Meta:
        verbose_name = _('TravelPlan')
        verbose_name_plural = _('TravelPlan')
        db_table = 'travelplan'

    def __str__(self):
        return self.tpname

class POIpoint(models.Model):
    pname = models.CharField(_('Name'), max_length=40)
    travelplan = models.ForeignKey(
        'cities.TravelPlan', verbose_name=_('TravelPlan'), on_delete=models.CASCADE, null=True, blank=True
    )
    point = models.PointField(verbose_name='Point', srid=4326, null=True, blank=True)
    objects = GeoManager()

    class Meta:
        verbose_name = _('POIpoint')
        verbose_name_plural = _('POIpoint')
        db_table = 'poipoint'

    def __str__(self):
        return self.pname

class NewMultiPoint(models.Model):
    name = models.CharField(max_length=40)
    nmp = models.MultiPointField()
    objects = GeoManager()

    class Meta:
        verbose_name = _('NewMultiPoint')
        verbose_name_plural = _('NewMultiPoint')
        db_table = 'newmultipoint'

    def __str__(self):
        return self.name

# class Location(models.Model):
#     name = models.CharField(max_length=255)
#     geopt = models.MultiPointField()
#
#     objects = GeoManager()
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = _('Location')
#         verbose_name_plural = _('Location')
#         db_table = 'location'

# class MushroomSpot(gismodels.Model):
#     name = models.CharField(max_length=256)
#     geom = gismodels.MultiPolygonField()
#     geoline = gismodels.LineStringField(blank=True, null=True)
#
#     objects = GeoManager()
#
#     def __unicode__(self):
#         return self.name

# class Marker(models.Model):
#     MarkerID= models.AutoField(primary_key=True)
#     name= models.CharField(max_length=40)
#     mpoint = models.PointField()
#     objects = GeoManager()
#     Latitude = models.DecimalField(max_digits=10, decimal_places=6)
#     Longitude = models.DecimalField(max_digits=10, decimal_places=6)
#
#     def save(self, *args, **kwargs):
#         self.Latitude  = self.mpoint.y
#         self.Longitude = self.mpoint.x
#         super(Marker, self).save(*args, **kwargs)
#
#     def __str__(self):
#         return self.name
