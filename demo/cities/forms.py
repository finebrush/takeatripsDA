from django import forms
from django.forms.models import inlineformset_factory

from demo.cities.models import ( City, InfoBasic, InfoTravel, TravelCurator, 
								TCImage, TravelPlan, POIpoint,
								EatDrinkPart, SeePart, SleepPart, BuyPart )

from dal import autocomplete
from mapwidgets.widgets import GooglePointFieldWidget
from material.base import Layout, Row, Column, Fieldset

from demo.common.models import CSmall

class TForm(forms.ModelForm):
	class Meta:
		model = TravelCurator
		fields = '__all__'
		widgets = {
			'infotravel' : autocomplete.ModelSelect2Multiple(
				url='tc-infotravel-autocomplete'
			)
		}

class CSForm(forms.ModelForm):
	class Meta:
		model = InfoTravel
		fields = '__all__'
		widgets = {
			'category' : autocomplete.ModelSelect2(
				url='cs-name-autocomplete'
			)
		}
# class POIpointAdminForm(forms.ModelForm):
# 	class Meta:
# 		model = POIpoint
# 		fields = ("point",)
# 		widgets = {
#             'point': GooglePointFieldWidget,
#         }

# class InfoTravelForm(forms.ModelForm):
# 	class Meta:
# 		model = InfoBasic
# 		fields = '__all__'
# 		layout = Layout(
# 					Fieldset('기본정보', 'city', 'companyko', 'companyeng', 'companyven'),
# 					Fieldset('대표이미지', 'pciture1', 'picture2', 'picture3', 'picture4'),
# 					Fieldset('일반정보', Row('part', 'typeit'), 'addressko', 'addresseng', 'addressven',
# 								'category', 'linkweb', 'linkinsta', 'linkyoutube', 'trafficko', 'trafficeng', 'trafficven',
# 								'introko', 'introeng', 'introven', 'tagko', 'tageng', 'tagven', 'itdate'),
# 					Fieldset('위치', 'itlocation')
#                     )

# class TravelCuratorForm(forms.ModelForm):
# 	layout = Layout(
# 					Fieldset('기본정보', 'city', 'titleko', 'titleeng', 'titleven', Row('created', 'writter')),
# 					Fieldset('대표이미지', 'picture1', 'picture2', 'picture3', 'picture4'),
# 					Fieldset('일반정보', 'introko', 'introeng', 'introven', 'tagko', 'tageng', 'tagven'),
# 					Fieldset('여행정보 추가', 'infotravel')
#                     )
# 	class Meta:
# 		# model = TravelCurator
# 		# fields = '__all__'

# 		widgets = {
# 			'infotravel' : autocomplete.ModelSelect2Multiple(
# 				url='tc-infotravel-autocomplete'
# 			)
# 		}
		