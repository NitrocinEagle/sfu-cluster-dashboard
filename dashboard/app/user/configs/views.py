# -*- coding: utf8 -*-
from __future__ import absolute_import
from mongoengine import connect
from django.views.generic import FormView
from .forms import MonitoringSettingsForm
from ..mixins import UserProfileMixin
from .form_handlers import (AddNodeHandler, AddServerGroupHandler,
                            AddNodeToGroupHandler, DelServerGroupHandler,
                            DelNodeFromGroupHandler)

connect("test_monitoring")


class MonitoringSettingsFormView(UserProfileMixin, FormView):
    form_class = MonitoringSettingsForm
    template_name = 'user/settings.html'
    success_url = '/user/settings/monitoring/'

    def form_valid(self, form):
        data = self.clean_form_data(form, self.request)
        op = data['operation']
        if op == 'add_node':
            AddNodeHandler(data).handle()
        if op == 'add_server_group':
            AddServerGroupHandler(data).handle()
        if op == 'del_server_group':
            DelServerGroupHandler(data).handle()
        if op == 'add_node_to_group':
            AddNodeToGroupHandler(data).handle()
        if op == 'del_node_from_group':
            DelNodeFromGroupHandler(data).handle()
        if op == 'stop_to_monitor_node':
            pass
        if op == 'stop_to_monitor_param':
            pass
        if op == 'change_param_timeout':
            pass

        return super(MonitoringSettingsFormView, self).form_valid(form)

    def form_invalid(self, form):
        return self.form_valid(form)

    def clean_form_data(self, form, request):
        data = {}
        for key in request._post.keys():
            data[key] = form.cleaned_data.get(key) or request._post[key]
        return data
