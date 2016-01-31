__author__ = 'mist'
from django.shortcuts import render
from django.views.generic import View
from dashboard.app.models import PluginInfo
from mongoengine import connect

connect("test")


class PluginsView(View):
    template_name = 'plugins/plugins.html'

    def get(self, request, *args, **kwargs):
        plugins_render = []

        plugins = PluginInfo.objects()
        for plugin in plugins:
            new_params = []
            params = plugin.params_info
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
        print plugins_render
        return render(request, self.template_name, {'plugins': plugins_render})
