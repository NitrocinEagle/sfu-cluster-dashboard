__author__ = 'mist'
from django.conf.urls import url, include

urlpatterns = [
    url(r'^dashboard/', include('app.dashboard.urls')),
    url(r'^plugins/', include('app.plugins.urls')),
]