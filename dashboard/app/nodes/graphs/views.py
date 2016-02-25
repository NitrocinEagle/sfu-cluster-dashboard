# -*- coding: utf-8 -*-
from __future__ import absolute_import
from django.shortcuts import render
from django.views.generic import View
from mongoengine import connect
from ...mongo_models import NodeInfo, ParamInfo

connect("test_monitoring")


class GraphsNodesView(View):
    template_name = 'graphs/graphs.html'

    def get(self, request, *args, **kwargs):
        graphs_info = []
        node_name = kwargs.get('node_name')
        node_plugins = NodeInfo.objects.get(node_name=node_name).enabled_plugins

        id = 1
        print 'node_plugins: ', node_plugins
        for plugin in node_plugins:
            params = ParamInfo.objects(plugin_name=plugin)
            for param in params:
                graphs_info.append(
                        {
                            "id": "graph_id_" + str(id),
                            "plugin_name": plugin,
                            "node_name": node_name,
                            "param_name": param.param_name
                        }
                )
                id += 1
        return render(request, self.template_name, {'graphs_info': graphs_info})
