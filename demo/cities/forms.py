from django import forms
from demo.cities.models import City, InfoBasic, InfoTravel, TravelCurator, TCImage, TravelPlan, POIpoint

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
