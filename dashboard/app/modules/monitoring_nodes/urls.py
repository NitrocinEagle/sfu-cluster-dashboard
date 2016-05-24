# -*- coding: utf8 -*-
from __future__ import absolute_import
from django.conf.urls import url, include
from .views import MonitoringView

urlpatterns = [
    url(r'^$', MonitoringView.as_view(), name="index"),
    url(r'^info/', include('app.modules.monitoring_nodes.info.urls', namespace='info')),
    url(r'^plugins/', include('app.modules.monitoring_nodes.plugins.urls', namespace="plugins")),
    url(r'^nodes/', include('app.modules.monitoring_nodes.nodes.urls', namespace="nodes")),
    url(r'^groups/', include('app.modules.monitoring_nodes.groups.urls', namespace="groups")),
    url(r'^graphs/', include('app.modules.monitoring_nodes.graphs.urls', namespace="graphs")),
    url(r'^configs/', include('app.modules.monitoring_nodes.configs.urls', namespace="configs")),
]
