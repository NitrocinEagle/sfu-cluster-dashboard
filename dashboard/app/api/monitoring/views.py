# -*- coding: utf8 -*-
from __future__ import absolute_import
from rest_framework.response import Response
from rest_framework.views import APIView
from ...mongo_models import MonitoringInfo
from mongoengine import connect

connect("test_monitoring")


class MonitoringInfoGet(APIView):
    http_method_names = ['get']


    def get(self, request, *args, **kwargs):
        # a = [
        #     {'header': 1, 'ip': 1, 'open': True, 'data': [
        #         {'header': 1, 'open': True, 'data': [
        #             {'param': 1, 'timeout': 1},
        #             {'param': 2, 'timeout': 2},
        #             {'param': 3, 'timeout': 3},
        #         ]},
        #         {'header': 2},
        #         {'header': 3},
        #     ]},
        #     {'header': 2, 'plugins': []},
        #     {'header': 3, 'plugins': []},
        # ]
        # data = []
        # nodes = []
        # [nodes.append({'node': item.node, 'ip': item.ip}) for item in MonitoringInfo.objects() if item.node not in nodes]
        # for node in nodes:
        #     data.append({'header': node, 'ip': node.ip, 'open': True, 'data': []})
        #     plugins = []
        #     [plugins.append(item.plugin) for item in MonitoringInfo.objects(node=node)]

        return Response({
            'result': 'success',
            'data': [{
                         'node': item['node'],
                         'ip': item['ip'],
                         'plugin': item['plugin'],
                         'timeout': item['timeout'],
                         'param': item['param'],
                     } for item in MonitoringInfo.objects()]
        })
