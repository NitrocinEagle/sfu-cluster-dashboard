# -*- coding: utf8 -*-
from __future__ import absolute_import
from ...mongo_models import MonitoringInfo
from ..views import BaseApiView
from mongoengine import connect

connect("test_monitoring")


class MonitoringInfoGet(BaseApiView):
    def get_data(self):
        return [{
                    'node': item['node'],
                    'ip': item['ip'],
                    'plugin': item['plugin'],
                    'timeout': item['timeout'],
                    'param': item['param'],
                } for item in MonitoringInfo.objects()]
