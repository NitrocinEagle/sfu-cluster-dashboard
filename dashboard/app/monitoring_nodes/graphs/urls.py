# -*- coding: utf8 -*-
from __future__ import absolute_import
from django.conf.urls import url
from .views import GraphsView, ShowGraphView

urlpatterns = [
    url(r'^$', GraphsView.as_view(), name='index'),
    url(r'^show/(?P<node_name>[^/]+)/(?P<plugin_name>[^/]+)/(?P<param_name>[^/]+)/$', ShowGraphView.as_view(), name='show_graph'),
]
