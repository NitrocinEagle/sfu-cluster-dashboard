# -*- coding: utf8 -*-
from __future__ import absolute_import
from django.views.generic import FormView, TemplateView
from .forms import ShowGraphForm
from app.mongo_models import MonitoringInfo


class GraphsView(FormView):
    template_name = "site/modules/monitoring_nodes/graphs/index.html"
    form_class = ShowGraphForm
    success_url = '/modules/monitoring_nodes/graphs'

    def form_valid(self, form):
        form_data = {}
        for key in form.data.keys():
            form_data[key] = form.data[key]
        return super(GraphsView, self).form_valid(form)

    def form_invalid(self, form):
        return self.form_valid(form)


class SingleGraphView(TemplateView):
    template_name = 'site/modules/monitoring_nodes/graphs/single_graph.html'

    def get_context_data(self, **kwargs):
        kwargs['graph'] = {
            'id': 1,
            'node_name': kwargs['node_name'],
            'plugin_name': kwargs['plugin_name'],
            'param_name': kwargs['param_name']
        }
        return super(SingleGraphView, self).get_context_data(**kwargs)


class NodeGraphsView(TemplateView):
    template_name = "site/modules/monitoring_nodes/graphs/graphs_node.html"

    def get_context_data(self, **kwargs):
        graphs_info = MonitoringInfo.objects.filter(node=kwargs['node_name'])
        kwargs['graphs_info'] = []
        for info in graphs_info:
            kwargs['graphs_info'].append({
                'id': len(kwargs['graphs_info']) + 1,
                'node_name': info.node,
                'plugin_name': info.plugin,
                'param_name': info.param
            })
        return super(NodeGraphsView, self).get_context_data(**kwargs)


class PluginGraphsView(TemplateView):
    template_name = "site/modules/monitoring_nodes/graphs/graphs_plugin.html"

    def get_context_data(self, **kwargs):
        graphs_info = MonitoringInfo.objects.filter(
            plugin=kwargs['plugin_name'])
        kwargs['graphs_info'] = []
        for info in graphs_info:
            kwargs['graphs_info'].append({
                'id': len(kwargs['graphs_info']) + 1,
                'node_name': info.node,
                'plugin_name': info.plugin,
                'param_name': info.param
            })
        return super(PluginGraphsView, self).get_context_data(**kwargs)


class ParamGraphsView(TemplateView):
    template_name = "site/modules/monitoring_nodes/graphs/graphs_param.html"

    def get_context_data(self, **kwargs):
        graphs_info = MonitoringInfo.objects.filter(param=kwargs['param_name'])
        kwargs['graphs_info'] = []
        for info in graphs_info:
            kwargs['graphs_info'].append({
                'id': len(kwargs['graphs_info']) + 1,
                'node_name': info.node,
                'plugin_name': info.plugin,
                'param_name': info.param
            })
        return super(ParamGraphsView, self).get_context_data(**kwargs)
