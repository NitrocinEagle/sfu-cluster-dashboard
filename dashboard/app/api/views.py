# -*- coding: utf8 -*-
from __future__ import absolute_import
from django.shortcuts import render
from django.views.generic import View
from rest_framework.response import Response
from rest_framework.views import APIView
from mongoengine import connect
from app.init_test_db.test_data import nodes_data, params_decription


connect("test")


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

        nodes_data_by_nodename = []
        nodes_data_by_pluginname = []
        filtered_node_data = None

        for node_data in nodes_data:
            if node_name == node_data['node_name']:
                nodes_data_by_nodename.append(node_data)

        for node_data in nodes_data_by_nodename:
            if plugin_name == node_data['plugin_name']:
                nodes_data_by_pluginname.append(node_data)

        for node_data in nodes_data_by_pluginname:
            if param_name == node_data['param_name']:
                filtered_node_data = node_data
                break

        graph_type = ''
        axis_y = ''
        axis_x = ''
        for param in params_decription:
            if filtered_node_data['param_name'] == param['param_name']:
                graph_type = param['graph_type']
                axis_y = param['axis_y_title']
                axis_x = param['axis_x_title']
                break

        if filtered_node_data is not None:
            return Response({
                'graph_type': graph_type,
                'graph_name': filtered_node_data['param_name'],
                'axis_y': axis_y,
                'axis_x': axis_x,
                'data': filtered_node_data['data']
            })
        return Response({
            'result': 'error',
            'code': 1
        })
