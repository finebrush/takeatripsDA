"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.views.generic import RedirectView
from django.contrib.staticfiles.templatetags.staticfiles import static as staticfiles

from material.admin.sites import site

from demo.cities.views import TCAutocomplete

site.site_header = _('T-A-T')
site.site_title = _('TaT')
site.favicon = staticfiles('donut_large.png')


urlpatterns = i18n_patterns(
    path('', include('clientapp.urls', namespace='clientend')),
    path('manager/', include('manager.urls', namespace='manager')),
    path('admin/', include('material.admin.urls')),
    # path('', RedirectView.as_view(url='admin/', permanent=False), name='index'),
    path('tc-infotravel-autocomplete/', TCAutocomplete.as_view(), name='tc-infotravel-autocomplete'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
