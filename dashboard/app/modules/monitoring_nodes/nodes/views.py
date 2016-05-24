# -*- coding: utf8 -*-
from __future__ import absolute_import
from django.shortcuts import render
from django.views.generic import View
from app.mongo_models import NodeInfo
from mongoengine import connect

connect("test_monitoring")
# connect('test', host='192.168.1.106', port=27017)


class NodesView(View):
    template_name = 'site/modules/monitoring_nodes/nodes/nodes.html'

    def get(self, request, *args, **kwargs):
        nodes_render = []
        nodes = NodeInfo.objects()
        for node in nodes:
            nodes_render.append({
                'name': node.node_name,
                'ip': node.node_ip,
                'os': node.node_os,
                'plugins': node.enabled_plugins
            })
        return render(request, self.template_name, {'nodes': nodes_render})
