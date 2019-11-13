from django.conf.urls import url, include
from django.views.generic.base import RedirectView
from django.views.generic import TemplateView

from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'manager'

# Redirect any request that goes into here to static/index.html
urlpatterns = [
    url(r'^$', views.post, name='main'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)