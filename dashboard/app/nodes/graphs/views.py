__author__ = 'mist'
from django.shortcuts import render
from django.views.generic import View
from ...models import NodeInfo
from mongoengine import connect

connect("test")


class GraphsPluginsView(View):
    template_name = 'graphs/graphs.html'


# Нужно выбрать из базы все узлы, у которых подключен конкретный плагин. И параметры тоже.
# Имя этого плагина должно лежать в кваргах
# Нужно получить что-то типа списка
lissst = {
    "plugin_name": "plugin",
    "nodes_params": [
        {
            "node_name": "1",
            "param_name": "1"
        },
        {
            "node_name": "2",
            "param_name": "2"
        },
    ]
}
# И в div уже пихать <div plugin_name="plugin" node_name="..." param_name="" class="graphs"></div>


def get(self, request, *args, **kwargs):
    nodes_render = []
    nodes = NodeInfo.objects()
    """for node in nodes:
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
    print plugins_render"""
    return render(request, self.template_name, {'nodes': nodes_render})
