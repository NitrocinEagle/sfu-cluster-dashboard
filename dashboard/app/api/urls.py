# -*- coding: utf8 -*-
from __future__ import absolute_import
from django.conf.urls import url, include
from .views import IndexAPIView, GraphsAPIView
urlpatterns = [
    url(r'$^', IndexAPIView.as_view()),
    url(r'configs/', include('app.api.configs.urls', namespace='configs')),
    url(r'monitoring/', include('app.api.monitoring.urls', namespace='monitoring')),
    url(r'^graphs/(?P<node_name>[^/]+)/(?P<plugin_name>[^/]+)/(?P<param_name>[^/]+)/$', GraphsAPIView.as_view()),
]