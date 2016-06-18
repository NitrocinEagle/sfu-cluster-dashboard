# -*- coding: utf8 -*-
from __future__ import absolute_import
from django.shortcuts import render
from django.views.generic import View
from rest_framework.response import Response
from rest_framework.views import APIView
from mongoengine import connect
from ..mongo_models import MonitoringNodesData, ParamInfo

connect("test_monitoring")


class BaseApiView(APIView):
    http_method_names = ['get']

    def get_data(self):
        raise BaseException("Redefine 'get_data'. It should return datalist.")

    def get(self, request, *args, **kwargs):
        try:
            return Response({
                'result': 'success',
                'data': self.get_data()
            })
        except:
            return Response({
                'result': 'error',
                'data': None
            })


class IndexAPIView(View):
    template_name = 'api/api.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class GraphsAPIView(APIView):
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        node_name = kwargs.get("node_name")
        plugin_name = kwargs.get("plugin_name")
        param_name = kwargs.get("param_name")
        print "request.GET: ", request.GET

        param_info = \
            ParamInfo.objects(plugin_name=plugin_name, param_name=param_name)[0]
        filter = {
            'node': node_name,
            'plugin': plugin_name,
            'param': param_name
        }
        count = MonitoringNodesData.objects(**filter).count()
        monitoring_data = MonitoringNodesData.objects(**filter)[
                          count - 20:count]

        metric = []
        if 'line_chart' in param_info.graph_types:
            for data in monitoring_data:
                metric.append({'value': data.data[param_name],
                               'timestamp': data.timestamp})

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
