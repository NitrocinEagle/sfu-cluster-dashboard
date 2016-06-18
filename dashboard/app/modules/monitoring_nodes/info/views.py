# -*- coding: utf8 -*-
from __future__ import absolute_import
from django.views.generic import TemplateView
from app.mongo_models import NodeInfo, MonitoringInfo
from mongoengine import connect

connect("test_monitoring")
# connect('test', host='192.168.1.106', port=27017)


class MonitoringInfoView(TemplateView):
    template_name = 'site/modules/monitoring_nodes/info/monitoring_info.html'

    def get_context_data(self, **kwargs):
        kwargs['monitoring_info'] = MonitoringInfo.objects()
        return super(MonitoringInfoView, self).get_context_data(**kwargs)
