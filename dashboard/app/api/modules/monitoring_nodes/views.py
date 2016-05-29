# -*- coding: utf8 -*-
from __future__ import absolute_import
from rest_framework.response import Response
from rest_framework.views import APIView
from app.mongo_models import MonitoringInfo
from mongoengine import connect

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
