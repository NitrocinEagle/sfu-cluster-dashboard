# -*- coding: utf8 -*-
from __future__ import absolute_import
from django.conf.urls import url
from .views import (GetServerGroupsAPIView, GetNodesAPIView, GetPluginsAPIView,
                    GetNodePluginsAPIView, GetParamsByNodePluginAPIView)

urlpatterns = [
    url(r'^get_server_groups/$', GetServerGroupsAPIView.as_view(),
        name='get-server-groups'),
    url(r'^get_nodes/$', GetNodesAPIView.as_view(),
        name='get-nodes'),
    url(r'^get_plugins/$', GetPluginsAPIView.as_view(),
        name='get-plugins'),
    url(r'^get_node_plugins/(?P<node_name>[^/]+)$',
        GetNodePluginsAPIView.as_view(),
        name='get-node-plugins'),
    url(
        r'^get_params_by_node_plugin/(?P<node_name>[^/]+)/(?P<plugin_name>[^/]+)$',
        GetParamsByNodePluginAPIView.as_view(),
        name='get-params-by-node-plugin'),
]
