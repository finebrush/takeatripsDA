from django import forms
from django.forms.models import inlineformset_factory

from demo.cities.models import ( City, InfoBasic, InfoTravel, TravelCurator, 
								TCImage, TravelPlan, POIpoint,
								EatDrinkPart, SeePart, SleepPart, BuyPart )

from dal import autocomplete
from mapwidgets.widgets import GooglePointFieldWidget

class TForm(forms.ModelForm):
	class Meta:
		model = TravelCurator
		fields = '__all__'
		widgets = {
			'infotravel' : autocomplete.ModelSelect2Multiple(
				url='tc-infotravel-autocomplete'
			)
		}

# class POIpointAdminForm(forms.ModelForm):
# 	class Meta:
# 		model = POIpoint
# 		fields = ("point",)
# 		widgets = {
#             'point': GooglePointFieldWidget,
#         }

# class CityForm(forms.ModelForm):
# 	layout = Layout('name', 'titleko', 'titleeng', 'titleven', 'created',
# 				Row('picture1', 'picture2', 'picture3', 'picture4'),
# 				Fieldset('location pick', 'location'))
# 	class Meta:
# 		model = City