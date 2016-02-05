# -*- coding: utf8 -*-
from __future__ import absolute_import
from django.shortcuts import render
from django.views.generic import View
from rest_framework.response import Response
from rest_framework.views import APIView
from mongoengine import connect
from time import time
import random
from ..models import NodeData, PluginInfo

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
        print 'node_name: ', node_name
        print 'plugin_name: ', plugin_name
        print 'param_name: ', param_name
        dataset_cpu_load = []
        dataset_ram_usage = []
        dataset_hdd_usage = []
        time_now = int(time())

        for i in range(10):
            dataset_cpu_load.append(
                {
                    "timestamp": time_now + i * 10,
                    "value": round(random.random() * 100, 2)
                }
            )
            dataset_ram_usage.append(
                {
                    "timestamp": time_now + i * 10,
                    "value": random.randint(512, 2048)
                }
            )
            dataset_hdd_usage.append(
                {
                    "timestamp": time_now + i * 3600,
                    "data": [
                        {
                            "sector_name": "Avaible",
                            "value": 50 * 1024,
                        },
                        {
                            "sector_name": "Used",
                            "value": 150 * 1024,
                        },
                    ]
                }
            )

        nodes_data = [
            {
                "node_name": "localhost",
                "node_ip": "127.0.0.1",
                "plugin_name": "cpu_load",
                "param_name": "cpu_load",
                "data": dataset_cpu_load
            },
            {
                "node_name": "localhost",
                "node_ip": "127.0.0.1",
                "plugin_name": "ram_usage",
                "param_name": "ram_usage",
                "data": dataset_ram_usage
            },
            {
                "node_name": "localhost",
                "node_ip": "127.0.0.1",
                "plugin_name": "hdd_usage",
                "param_name": "hdd_usage",
                "data": dataset_hdd_usage
            },
            {
                "node_name": "first",
                "node_ip": "192.168.0.1",
                "plugin_name": "cpu_load",
                "param_name": "cpu_load",
                "data": dataset_cpu_load
            },
            {
                "node_name": "first",
                "node_ip": "192.168.0.1",
                "plugin_name": "ram_usage",
                "param_name": "ram_usage",
                "data": dataset_ram_usage
            },
            {
                "node_name": "first",
                "node_ip": "192.168.0.1",
                "plugin_name": "hdd_usage",
                "param_name": "hdd_usage",
                "data": dataset_hdd_usage
            },
            {
                "node_name": "second",
                "plugin_name": "cpu_load",
                "param_name": "cpu_load",
                "data": dataset_cpu_load
            },
            {
                "node_name": "second",
                "node_ip": "192.168.0.2",
                "plugin_name": "ram_usage",
                "param_name": "ram_usage",
                "data": dataset_ram_usage
            },
            {
                "node_name": "second",
                "node_ip": "192.168.0.2",
                "plugin_name": "hdd_usage",
                "param_name": "hdd_usage",
                "data": dataset_hdd_usage
            },
        ]

        # print NodeData.objects(node_name=node_name)[0]
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

        if filtered_node_data is not None:
            return Response({
                'graph_type': '',
                'graph_name': filtered_node_data['param_name'],
                'axis_y': '',
                'axis_x': '',
                'data': filtered_node_data['data']
            })
        else:
            return Response({
                'result': 'error',
                'code': 1
            })
