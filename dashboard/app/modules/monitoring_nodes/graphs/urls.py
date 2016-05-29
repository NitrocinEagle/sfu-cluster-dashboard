# -*- coding: utf8 -*-
from __future__ import absolute_import
from django.conf.urls import url
from .views import (GraphsView, SingleGraphView, NodeGraphsView,
                    PluginGraphsView, ParamGraphsView)

urlpatterns = [
    url(r'^$', GraphsView.as_view(), name='index'),
    url(r'^show/(?P<node_name>[^/]+)/(?P<plugin_name>[^/]+)/(?P<param_name>[^/]+)/$', SingleGraphView.as_view(), name='show_graph'),
    url(r'^node-graphs/(?P<node_name>[^/]+)/$', NodeGraphsView.as_view(), name='node_graphs'),
    url(r'^plugin-graphs/(?P<plugin_name>[^/]+)/$', PluginGraphsView.as_view(), name='plugin_graphs'),
    url(r'^param-graphs/(?P<param_name>[^/]+)/$', ParamGraphsView.as_view(), name='param_graphs'),
]
