__author__ = 'mist'
from django.conf.urls import url
from views import PluginsView

urlpatterns = [
    url(r'^$', PluginsView.as_view()),
]