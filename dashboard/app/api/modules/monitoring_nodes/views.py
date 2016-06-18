# -*- coding: utf8 -*-
from __future__ import absolute_import
from rest_framework.response import Response
from rest_framework.views import APIView
from app.mongo_models import MonitoringInfo, ParamInfo, MonitoringNodesData
from mongoengine import connect
from datetime import datetime, timedelta
import time

connect("test_monitoring")


class GetNodesListAPIView(APIView):
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        nodes = MonitoringInfo.objects.distinct("node")
        if nodes:
            return Response({
                'result': 'success',
                'data': nodes
            })
        return Response({
            'result': 'error',
            'code': 1
        })


class GetPluginsListAPIView(APIView):
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        plugins = MonitoringInfo.objects.distinct("plugin")
        if plugins:
            return Response({
                'result': 'success',
                'data': plugins
            })
        return Response({
            'result': 'error',
            'code': 1
        })


class GetParamsListAPIView(APIView):
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        params = MonitoringInfo.objects.distinct("param")
        if params:
            return Response({
                'result': 'success',
                'data': params
            })
        return Response({
            'result': 'error',
            'code': 1
        })


class GetMonitoringDataAPIView(APIView):
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        qs = request.GET
        node_name = qs.get("node_name")
        plugin_name = qs.get("plugin_name")
        param_name = qs.get("param_name")
        time_from = qs.get("time_from")
        time_to = qs.get("time_to")
        selected_time = qs.get("selected_time")

        day_before_now = datetime.now() - timedelta(days=1)
        day_before_now = time.mktime(day_before_now.timetuple())

        time_to = time_to if time_to else time.mktime(
            datetime.now().timetuple())
        time_from = time_from if time_from else day_before_now

        param_info = \
        ParamInfo.objects(plugin_name=plugin_name, param_name=param_name)[0]
        filter = {
            'node': node_name,
            'plugin': plugin_name,
            'param': param_name,
            'stamp__lt': time_to,
            'stamp__gt': time_from,
        }
        # count = MonitoringNodesData.objects(**filter).count()


        metric = []
        if 'pie_chart' in param_info.graph_types:
            data = MonitoringNodesData.objects(**filter)[0].data
            param_key = data.keys()[0]
            for k, v in data[param_key].items():
                if k != 'percent':
                    metric.append({'value': v, 'sector_name': k})
            return Response({
                'graph_types': param_info.graph_types,
                'graph_name': param_key,
                'axis_y': param_info.axis_y_title,
                'axis_x': param_info.axis_x_title,
                'data': metric
            })

        if 'line_chart' in param_info.graph_types:
            for data in MonitoringNodesData.objects(**filter):
                metric.append({'value': data.data[param_name],
                               'timestamp': data.stamp})

        if metric and param_info:
            return Response({
                'graph_types': param_info.graph_types,
                'graph_name': param_info.param_name,
                'axis_y': param_info.axis_y_title,
                'axis_x': param_info.axis_x_title,
                'data': metric
            })

        return Response({
            'result': 'error',
            'code': 1
        })
