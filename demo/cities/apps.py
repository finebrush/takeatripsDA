from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CitiesConfig(AppConfig):
    name = 'demo.cities'
    icon_name = 'location_city'
    verbose_name = _('Cities')
