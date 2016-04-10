# -*- coding: utf8 -*-
from __future__ import absolute_import
from rest_framework.response import Response
from rest_framework.views import APIView
from mongoengine import connect
from ...mongo_models import NodeInfo, ParamInfo, NodeGroups

connect("test_monitoring")


class GetServerGroupsAPIView(APIView):
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        return Response({
            'result': 'success',
            'groups': [node_group.name for node_group in NodeGroups.objects()],
        })


class GetNodesAPIView(APIView):
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        return Response({
            'result': 'success',
            'nodes': [node_info.node_name for node_info in NodeInfo.objects()],
        })


class GetPluginsAPIView(APIView):
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        return Response({
            'result': 'success',
            'plugins': [item.node_name for item in NodeInfo.objects()],
        })


class GetNodePluginsAPIView(APIView):
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        node_name = kwargs.get('node_name')
        if node_name:
            return Response({
                'result': 'success',
                'plugins': NodeInfo.objects(
                    node_name=node_name).first().enabled_plugins,
            })
        return Response({
            'plugins': ['plugin12', 'plugin32'],
        })


class GetParamsByNodePluginAPIView(APIView):
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        node_name = kwargs.get('node_name')
        plugin_name = kwargs.get('plugin_name')
        if node_name and plugin_name:
            if plugin_name in NodeInfo.objects(
                    node_name=node_name).first().enabled_plugins:
                params = [param_info.param_name for param_info in
                          ParamInfo.objects(plugin_name=plugin_name)]
            return Response({
                'result': 'success',
                'params': params,
            })
        return Response({
            'result': 'error',
            'code': 1
        })
