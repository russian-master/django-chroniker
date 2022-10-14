from django.urls import re_path as url, include

from django.core.exceptions import ImproperlyConfigured
from django.contrib import admin

admin.autodiscover()

try:
    _patterns = [
        url(r'^admin/', include(admin.site.urls)),
    ]
except ImproperlyConfigured:
    # Django >= 2.1.7.
    _patterns = [
        url(r'^admin/', admin.site.urls),
    ]

urlpatterns = _patterns
