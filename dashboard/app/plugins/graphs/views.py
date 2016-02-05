# -*- coding: utf8 -*-
from __future__ import absolute_import
from django.shortcuts import render
from django.views.generic import View
from ...models import NodeInfo, PluginInfo
from mongoengine import connect

connect("test")


class GraphsPluginsView(View):
    template_name = 'graphs/graphs.html'

    def get(self, request, *args, **kwargs):
        # uncomment it if there is workable DB
        """
        graphs_info = []
        plugin_name = kwargs.get('plugin_name')  # TODO: add 'try ... except'
        plugin_params = [param.param_name for param in PluginInfo.objects(
                plugin_name=plugin_name).params_info]
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
                                "param_name": param
                            }
                    )
                    id += 1
        """
        # uncomment it if there is workable DB
        test_graphs_info = [
            {
                "id": "graph_id_1",
                "plugin_name": "cpu_load",
                "node_name": "node_1",
                "param_name": "cpu_load"
            },
            {
                "id": "graph_id_2",
                "plugin_name": "cpu_load",
                "node_name": "node_2",
                "param_name": "cpu_load"
            },
            {
                "id": "graph_id_2",
                "plugin_name": "cpu_load",
                "node_name": "node_2",
                "param_name": "cpu_load"
            }
        ]
        return render(request, self.template_name,{'graphs_info': test_graphs_info})
        # uncomment it if there is workable DB
        #return render(request, self.template_name,{'graphs_info': graphs_info})
