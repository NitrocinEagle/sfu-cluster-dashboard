# -*- coding: utf8 -*-
from __future__ import absolute_import
from rest_framework.response import Response
from rest_framework.views import APIView
from mongoengine import connect
from ...mongo_models import NodeInfo, ParamInfo, NodeGroups, PluginInfo

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


class GetServerGroupsAPIView(BaseApiView):
    def get_data(self):
        return [node_group.name for node_group in NodeGroups.objects()]


class GetNodesAPIView(BaseApiView):
    def get_data(self):
        return [node_info.node_name for node_info in NodeInfo.objects()]


class GetNodesByGroupAPIView(BaseApiView):
    def get_data(self):
        group = self.kwargs.get('group_name')
        return NodeGroups.objects(name=group).first().enabled_nodes


class GetPluginsAPIView(BaseApiView):
    def get_data(self):
        return [item.plugin_name for item in PluginInfo.objects()]


class GetNodePluginsAPIView(BaseApiView):
    def get_data(self):
        node_name = self.kwargs.get('node_name')
        if node_name:
            return NodeInfo.objects(node_name=node_name).first().enabled_plugins
        return ['plugin12', 'plugin32']


class GetParamsByNodePluginAPIView(BaseApiView):
    def get_data(self):
        node_name = self.kwargs.get('node_name')
        plugin_name = self.kwargs.get('plugin_name')
        if node_name and plugin_name:
            if plugin_name in NodeInfo.objects(
                    node_name=node_name).first().enabled_plugins:
                params = [param_info.param_name for param_info in
                          ParamInfo.objects(plugin_name=plugin_name)]
            return params
        return []
