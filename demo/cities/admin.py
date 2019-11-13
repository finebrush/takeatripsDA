from django.contrib import admin
from django.contrib.gis.db import models
# import os
from demo.cities.models import City, InfoBasic, InfoTravel, TravelCurator, TCImage, TravelPlan, POIpoint, NewMultiPoint
from material.admin.decorators import register
from material.admin.options import MaterialModelAdmin
from imagekit.admin import AdminThumbnail
from .widgets import AdminImageWidget
from .forms import TForm
from django.contrib.admin.options import FORMFIELD_FOR_DBFIELD_DEFAULTS
from django.contrib.gis import admin

from leaflet.admin import LeafletGeoAdmin

from mapwidgets.widgets import GooglePointFieldWidget, GooglePointFieldInlineWidget

CUSTOM_MAP_SETTINGS = {
    "GooglePointFieldWidget": (
        ("zoom", 10),
        ("mapCenterLocation", [37.59675, 126.99488]),
    ),
}

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

class POIpointInline(admin.StackedInline):
    model = POIpoint
    ordering = ('id',)
    extra = 0
    # can_delete = False
    # verbose_name_plural = 'POIpoint'

    formfield_overrides = {
        models.PointField: {"widget": GooglePointFieldInlineWidget}
    }

@register(City)
class CityAdmin(LeafletGeoAdmin):
    list_display = ('name', 'titleko', 'titleeng', 'titleven', 'created', 'picture_tag', 'location')
    icon_name = 'location_city'
    search_fields = ('name',)
    # inlines = [InfoBasicInline, InfoTravelInline]

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

    # form 안에 이미지 나타내기..
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'ibrepicture':
            kwargs.pop("request", None)
            kwargs['widget'] = AdminImageWidget
            return db_field.formfield(**kwargs)
        return super(InfoBasicAdmin,self).formfield_for_dbfield(db_field, **kwargs)

@register(InfoTravel)
class InfoTavelAdmin(LeafletGeoAdmin):
    icon_name = 'edit_location'
    # autocomplete_fields = ('ibname', 'city')
    list_display = ('companyko', 'picture_tag', 'part', 'category', 'itlocation')

    # (2) Show thumbnail in changeview..form 에서 이미지 보여줌..
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'picture1' or db_field.name == 'picture2' or db_field.name == 'picture3' or db_field.name == 'picture4':
            # remove request to avoid "__init__() got an unexpected keyword argument 'request'" error
            kwargs.pop("request", None)
            kwargs['widget'] = AdminImageWidget
            return db_field.formfield(**kwargs)
        return super(InfoTavelAdmin,self).formfield_for_dbfield(db_field, **kwargs)

@register(TravelCurator)
class TravelCuratorAdmin(MaterialModelAdmin):
    form = TForm
    list_display = ('tctitle', 'tcwritter')
    icon_name = 'departure_board'
    inlines = [TCImageInline]

@register(TravelPlan)
class TravelPlanAdmin(MaterialModelAdmin):
    icon_name = 'edit_location'
    list_display = ('tpname', 'tpcomment')
    inlines = [POIpointInline]

@register(POIpoint)
class POIpointAdmin(MaterialModelAdmin):
    icon_name = 'edit_location'
    list_display = ('pname', 'point')
    formfield_overrides = {
        models.PointField: {"widget": GooglePointFieldWidget(settings=CUSTOM_MAP_SETTINGS)}
    }

@register(NewMultiPoint)
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
