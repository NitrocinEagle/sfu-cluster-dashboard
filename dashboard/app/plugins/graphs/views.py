# -*- coding: utf8 -*-
from __future__ import absolute_import
from django.shortcuts import render
from django.views.generic import View
from ...mongo_models import NodeInfo, PluginInfo, ParamInfo
from mongoengine import connect

connect("test_monitoring")


class GraphsPluginsView(View):
    template_name = 'graphs/graphs.html'

    def get(self, request, *args, **kwargs):
        graphs_info = []
        plugin_name = kwargs.get('plugin_name')
        # TODO: add 'try ... except'
        plugin_params = ParamInfo.objects(plugin_name=plugin_name)
        nodes = NodeInfo.objects()
        id = 1
        for node in nodes:
            if plugin_name in node.enabled_plugins:
                for param in plugin_params:
                    graphs_info.append(
                            {
                                "id": "graph_id_" + str(id),
                                "plugin_name": plugin_name,
                                "node_name": node.node_name,
                                "param_name": param.param_name
                            }
                    )
                    id += 1

        return render(request, self.template_name, {'graphs_info': graphs_info})
