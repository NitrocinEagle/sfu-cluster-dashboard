# -*- coding: utf8 -*-
from __future__ import absolute_import
from django.views.generic import TemplateView
from app.mongo_models import (PluginInfo, NodeInfo, ParamInfo, NodeGroups)
from mongoengine import connect

connect("test_monitoring")


# connect('test', host='192.168.1.106', port=27017)

class MonitoringView(TemplateView):
    template_name = 'site/modules/monitoring_nodes/index.html'

    def get_context_data(self, **kwargs):
        kwargs['plugins'] = PluginInfo.objects.all()
        nodes = [x for x in NodeInfo.objects.all()]
        for node in nodes:
            node['enabled_plugins'] = ', '.join(node['enabled_plugins'])
        kwargs['nodes'] = nodes
        kwargs['groups'] = NodeGroups.objects.all()
        return super(MonitoringView, self).get_context_data(**kwargs)