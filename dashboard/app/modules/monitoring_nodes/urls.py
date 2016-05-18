# -*- coding: utf8 -*-
from __future__ import absolute_import
from django.conf.urls import url, include
from .views import MonitoringView, MonitoringInfoView

urlpatterns = [
    url(r'^$', MonitoringView.as_view(), name="index"),
    url(r'^info/', MonitoringInfoView.as_view(), name="info"),
    url(r'^plugins/', include('app.monitoring_nodes.plugins.urls', namespace="plugins")),
    url(r'^nodes/', include('app.monitoring_nodes.nodes.urls', namespace="nodes")),
    url(r'^groups/', include('app.monitoring_nodes.groups.urls', namespace="groups")),
    url(r'^graphs/', include('app.monitoring_nodes.graphs.urls', namespace="graphs")),
]
