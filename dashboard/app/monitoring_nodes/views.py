# -*- coding: utf8 -*-
from __future__ import absolute_import
from django.views.generic import TemplateView
from app.mongo_models import (MonitoringInfo, PluginInfo, NodeInfo, ParamInfo,
                              NodeGroups)
from mongoengine import connect

connect("test_monitoring")


# connect('test', host='192.168.1.106', port=27017)

class MonitoringView(TemplateView):
    template_name = 'monitoring_nodes/index.html'


class MonitoringInfoView(TemplateView):
    template_name = 'monitoring_nodes/monitoring.html'

    def get_context_data(self, **kwargs):
        print MonitoringInfo.objects()
        kwargs['monitoring_info'] = MonitoringInfo.objects()
        return super(MonitoringInfoView, self).get_context_data(**kwargs)
