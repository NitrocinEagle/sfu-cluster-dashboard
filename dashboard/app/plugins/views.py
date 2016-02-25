# -*- coding: utf8 -*-
from __future__ import absolute_import
from django.shortcuts import render
from django.views.generic import View
from ..mongo_models import PluginInfo, ParamInfo
from mongoengine import connect

connect("test_monitoring")


# connect('test', host='192.168.1.106', port=27017)


class PluginsView(View):
    template_name = 'plugins/plugins.html'

    def get(self, request, *args, **kwargs):
        plugins_render = []

        plugins = PluginInfo.objects()
        for plugin in plugins:
            new_params = []
            params = ParamInfo.objects(plugin_name=plugin.plugin_name)
            for param in params:
                new_params.append({
                    'name': param.param_name,
                    'description': param.description,
                    'timeout': param.timeout
                })
            plugins_render.append({
                'name': plugin.plugin_name,
                'description': plugin.description,
                'params_info': new_params
            })
        return render(request, self.template_name, {'plugins': plugins_render})
