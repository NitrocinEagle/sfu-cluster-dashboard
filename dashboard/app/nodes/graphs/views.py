# -*- coding: utf-8 -*-
from __future__ import absolute_import
from django.shortcuts import render
from django.views.generic import View
from mongoengine import connect
from ...mongo_models import NodeInfo, PluginInfo

connect("test")


class GraphsNodesView(View):
    template_name = 'graphs/graphs.html'

    def get(self, request, *args, **kwargs):
        # uncomment it if there is workable DB
        """
        graphs_info = []
        node_name = kwargs.get('node_name')  # TODO: add 'try ... except'
        node = NodeInfo.objects(node_name=node_name)
        node_plugins = node.enabled_plugins
        id = 1
        for plugin in node_plugins:
            plugin_params = [param.param_name for param in
                             PluginInfo.objects(plugin_name=plugin).params_info]
            for param in plugin_params:
                graphs_info.append(
                        {
                            "id": "graph_id_" + str(id),
                            "plugin_name": plugin,
                            "node_name": node_name,
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
                "plugin_name": "ram_usage",
                "node_name": "node_1",
                "param_name": "ram_usage"
            },
            {
                "id": "graph_id_3",
                "plugin_name": "hdd_usage",
                "node_name": "node_1",
                "param_name": "hdd_usage"
            }
        ]

        return render(request, self.template_name, {'graphs_info': test_graphs_info})
        # uncomment it if there is workable DB
        # return render(request, self.template_name, {'graphs_info': graphs_info})
