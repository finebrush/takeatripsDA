from dal import autocomplete

from demo.cities.models import City, InfoBasic, InfoTravel, TravelCurator, TCImage
from demo.common.models import CSmall

class TCAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        # if not self.request.user.is_authenticated():
        #     return Country.objects.none()

        qs = InfoTravel.objects.all()

        if self.q:
            qs = qs.filter(companyko__contains=self.q)

        return qs

class CSAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = CSmall.objects.all()
        if self.q:  # cs-name-autocomplete/?q= 와 같은..
            qs = qs.filter(name__contains=self.q)

        return qs