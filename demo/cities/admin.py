from django.contrib import admin
from django.contrib.gis.db import models
# import os
from demo.cities.models import ( City, InfoBasic, InfoTravel, TravelCurator, 
                                TCImage, TravelPlan, POIpoint, PointImage, NewMultiPoint, 
                                EatDrinkPart, SeePart, SleepPart, BuyPart ) 

from material.admin.decorators import register
from material.admin.options import MaterialModelAdmin
from imagekit.admin import AdminThumbnail
from .widgets import AdminImageWidget
from .forms import TForm, CSForm# , TravelCuratorForm, InfoTravelForm, 
from django.contrib.admin.options import FORMFIELD_FOR_DBFIELD_DEFAULTS
from django.contrib.gis import admin

from leaflet.admin import LeafletGeoAdmin

from mapwidgets.widgets import GooglePointFieldWidget, GooglePointFieldInlineWidget

from material.base import Layout, Row, Column, Fieldset
from fieldsets_with_inlines import FieldsetsInlineMixin

CUSTOM_MAP_SETTINGS = {
    "GooglePointFieldWidget": (
        ("zoom", 10),
        ("mapCenterLocation", [37.59675, 126.99488]),
    ),
}

class EatDrinkPartInline(admin.StackedInline):
    model = EatDrinkPart
    extra = 1
    can_delete = False

class SeePartInline(admin.StackedInline):
    model = SeePart
    extra = 1
    can_delete = False

class SleepPartInline(admin.StackedInline):
    model = SleepPart
    extra = 1
    can_delete = False

class BuyPartInline(admin.StackedInline):
    model = BuyPart
    extra = 1
    can_delete = False

class InfoBasicInline(admin.StackedInline):
    model = InfoBasic
    ordering = ('id',)
    extra = 0

class InfoTravelInline(admin.StackedInline):
    model = InfoTravel
    ordering = ('id',)
    extra = 0

class TCImageInline(admin.StackedInline):
    model = TCImage
    ordering = ('id',)
    extra = 0

class PointImageInline(admin.StackedInline):
    model = PointImage
    ordering = ('id',)
    extra = 0

class POIpointInline(admin.StackedInline):
    model = POIpoint
    ordering = ('id',)
    extra = 0
    # can_delete = False
    # verbose_name_plural = 'POIpoint'

    formfield_overrides = {
        models.PointField: {"widget": GooglePointFieldInlineWidget}
    }

class NewMultiPointInline(admin.StackedInline):
    model = NewMultiPoint
    ordering = ('id',)
    extra = 0
    
@register(City)
class CityAdmin(MaterialModelAdmin):
    list_display = ('name', 'titleko', 'titleeng', 'titleven', 'created', 'picture_tag', 'location')
    icon_name = 'location_city'
    search_fields = ('name',)
    list_per_page = 10
    # inlines = [InfoBasicInline, InfoTravelInline]

    # 표시할 필드 순서.. 넣지않으면 나타나지 않음..
    # fields = ['name', 'created', 'titleko', 'titleeng', 'titleven', 'location']

    # 각 필드를 구분하는 대표제목을 설정한다. (리스트 내 튜플)
    fieldsets = [
        ('기본 정보',   {'fields': ['name', 'created','titleko', 'titleeng', 'titleven']}),
        ('대표 이미지',  {'fields': ['picture1', 'picture2', 'picture3', 'picture4']}),
        ('위치',       {'fields': ['location']}),
    ]

    formfield_overrides = {
        models.PointField: {"widget": GooglePointFieldWidget(settings=CUSTOM_MAP_SETTINGS)}
    }

    # form 안에 이미지 나타내기..
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'picture1' or db_field.name == 'picture2' or db_field.name == 'picture3' or db_field.name == 'picture4':
            kwargs.pop("request", None)
            kwargs['widget'] = AdminImageWidget
            return db_field.formfield(**kwargs)
        return super(CityAdmin,self).formfield_for_dbfield(db_field, **kwargs)


# @register(InfoBasic)
class InfoBasicAdmin(MaterialModelAdmin):
    icon_name = 'info'
    # autocomplete_fields = ('ibname', 'city')
    list_display = ('ibname', 'ibtitle', 'ibrepicture_tag')
    search_fields = ('ibname',)

    # form 안에 이미지 나타내기..
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'ibrepicture':
            kwargs.pop("request", None)
            kwargs['widget'] = AdminImageWidget
            return db_field.formfield(**kwargs)
        return super(InfoBasicAdmin,self).formfield_for_dbfield(db_field, **kwargs)

@register(InfoTravel)
class InfoTavelAdmin(MaterialModelAdmin):
    # form = CSForm
    icon_name = 'edit_location'
    # autocomplete_fields = ('ibname', 'city')
    list_display = ('companyko', 'picture_tag', 'part', 'category', 'itlocation')
    search_fields = ('companyko', 'companyeng', 'companyven',)
    inlines = [EatDrinkPartInline, SeePartInline, SleepPartInline, BuyPartInline,]
    list_per_page = 10
    list_filter = ('part',)

    fieldsets = [
        ('기본 정보',   {'fields': ['city', 'itdate', 'companyko', 'companyeng', 'companyven']}),
        ('대표 이미지',  {'fields': ['picture1', 'picture2', 'picture3', 'picture4'], 'classes': ['collapse']}),
        ('일반 정보',  {'fields': ['part', 'typeit', 'addressko', 'addresseng','addressven', 'category',
                                    'linkweb', 'linkinsta', 'linkyoutube', 'trafficko', 'trafficeng', 'trafficven',
                                    'introko', 'introeng', 'introven', 'tagko', 'tageng', 'tagven'], 'classes': ['collapse']}),
        ('위치',       {'fields': ['itlocation']}),
    ]

    formfield_overrides = {
        models.PointField: {"widget": GooglePointFieldWidget(settings=CUSTOM_MAP_SETTINGS)}
    }

    # (2) Show thumbnail in changeview..form 에서 이미지 보여줌..
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'picture1' or db_field.name == 'picture2' or db_field.name == 'picture3' or db_field.name == 'picture4':
            # remove request to avoid "__init__() got an unexpected keyword argument 'request'" error
            kwargs.pop("request", None)
            kwargs['widget'] = AdminImageWidget
            return db_field.formfield(**kwargs)
        return super(InfoTavelAdmin,self).formfield_for_dbfield(db_field, **kwargs)

    class Media:
        js = (
                'https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js',
                '/static/admin/js/fbinlineonoff.js',
            )

@register(TravelCurator)
class TravelCuratorAdmin(FieldsetsInlineMixin, MaterialModelAdmin):
    form = TForm
    # form = TravelCuratorForm
    list_display = ('titleko', 'created')
    icon_name = 'departure_board'
    # inlines = [TCImageInline]
    fieldsets_with_inlines = [
        ('기본정보', {'fields': ['city', 'titleko', 'titleeng', 'titleven', 'created', 'writter']}),
        # ('대표이미지', {'fields': ['picture1', 'picture2', 'picture3', 'picture4']}),
        TCImageInline,
        ('일반정보', {'fields': ['introko', 'introeng', 'introven', 'tagko', 'tageng', 'tagven']}),
        ('여행장소', {'fields': ['infotravel',]})
    ]
@register(TCImage)
class TCImageAdmin(MaterialModelAdmin):
    icon_name = 'edit_location'
    list_display = ('travelcurator', 'picture_tag')

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'tcimg':
            # remove request to avoid "__init__() got an unexpected keyword argument 'request'" error
            kwargs.pop("request", None)
            kwargs['widget'] = AdminImageWidget
            return db_field.formfield(**kwargs)
        return super(TCImageAdmin,self).formfield_for_dbfield(db_field, **kwargs)

@register(TravelPlan)
class TravelPlanAdmin(MaterialModelAdmin):
    icon_name = 'edit_location'
    list_display = ('titleko', 'inlinecount', 'created')
    inlines = [POIpointInline]

@register(POIpoint)
class POIpointAdmin(MaterialModelAdmin):
    icon_name = 'edit_location'
    list_display = ('pnameko', 'point')
    formfield_overrides = {
        models.PointField: {"widget": GooglePointFieldWidget(settings=CUSTOM_MAP_SETTINGS)}
    }

# @register(PointImage)
class PointImageAdmin(MaterialModelAdmin):
    icon_name = 'edit_location'
    list_display = ('picture_tag',)

# @register(NewMultiPoint)
class NewMultiPointAdmin(LeafletGeoAdmin):
    icon_name = 'edit_location'
    list_display = ('name', 'nmp')
    

# @register(Location)
# class LocationAdmin(MaterialModelAdmin):
#     icon_name = 'edit_location'
#     list_display = ('name', 'geopt')
#     formfield_overrides = {
#         models.MultiPointField: {"widget": GooglePointFieldWidget}
#     }

# @register(MushroomSpot)
# class MushroomSpotAdmin(LeafletGeoAdmin):
#     icon_name = 'edit_location'
#     list_display = ('name', 'geoline')
#
# @register(Marker)
# class MarkerAdmin(LeafletGeoAdmin):
#     icon_name = 'edit_location'
#     list_display = ('name',)
#     # readonly_fields = ('Latitude','Longitude')
