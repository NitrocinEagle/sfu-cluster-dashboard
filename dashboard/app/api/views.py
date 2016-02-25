# -*- coding: utf8 -*-
from __future__ import absolute_import
from django.shortcuts import render
from django.views.generic import View
from rest_framework.response import Response
from rest_framework.views import APIView
from mongoengine import connect
from ..init_test_db.test_data import nodes_data, params_info
from ..mongo_models import NodeData, ParamInfo

connect("test_monitoring")


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

        node_data = NodeData.objects(node_name=node_name, plugin_name=plugin_name, param_name=param_name)[0].data
        param_info = ParamInfo.objects(plugin_name=plugin_name, param_name=param_name)[0]

        if node_data and param_info:
            return Response({
                'graph_type': param_info.graph_type,
                'graph_name': param_info.param_name,
                'axis_y': param_info.axis_y_title,
                'axis_x': param_info.axis_x_title,
                'data': node_data
            })

        return Response({
            'result': 'error',
            'code': 1
        })
