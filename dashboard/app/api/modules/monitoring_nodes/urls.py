# -*- coding: utf8 -*-
from __future__ import absolute_import
from django.conf.urls import url
from .views import (GetParamsListAPIView, GetNodesListAPIView,
                    GetPluginsListAPIView, GetMonitoringDataAPIView)

urlpatterns = [
    url(r'get-nodes-list/', GetNodesListAPIView.as_view(),
        name='get_nodes_list'),
    url(r'get-plugins-list/', GetPluginsListAPIView.as_view(),
        name='get_plugins_list'),
    url(r'get-params-list/', GetParamsListAPIView.as_view(),
        name='get_params_list'),
    url(r'get-monitoring-data/', GetMonitoringDataAPIView.as_view(),
        name='get_monitoring_data'),
]
