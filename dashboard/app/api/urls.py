# -*- coding: utf8 -*-
from __future__ import absolute_import
from django.conf.urls import url
from .views import IndexAPIView, GraphsAPIView
urlpatterns = [
    url(r'$^', IndexAPIView.as_view()),
    url(r'^graphs/(?P<node_name>[^/]+)/(?P<plugin_name>[^/]+)/(?P<param_name>[^/]+)/$', GraphsAPIView.as_view()),
]