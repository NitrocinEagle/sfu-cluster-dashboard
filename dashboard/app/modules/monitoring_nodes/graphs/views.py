# -*- coding: utf8 -*-
from __future__ import absolute_import
from django.views.generic import FormView, TemplateView
from .forms import ShowGraphForm


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


class ShowGraphView(TemplateView):
    template_name = 'site/modules/monitoring_nodes/graphs/graph.html'

    def get_context_data(self, **kwargs):
        kwargs['graphs_info'] = [{
            'id': 1,
            'node_name': kwargs['node_name'],
            'plugin_name': kwargs['plugin_name'],
            'param_name': kwargs['param_name']
        }]
        return super(ShowGraphView, self).get_context_data(**kwargs)
