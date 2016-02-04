# -*- coding: utf8 -*-
from __future__ import absolute_import
from django.conf.urls import url, include
from .views import PluginsView

urlpatterns = [
    url(r'^$', PluginsView.as_view()),
    url(r'^(?P<plugin_name>\w+)/graphs/', include('app.plugins.graphs.urls')),
]