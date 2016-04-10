# -*- coding: utf8 -*-
from __future__ import absolute_import
from mongoengine import connect
from django.views.generic import FormView
from .forms import MonitoringSettingsForm
from ..mixins import UserProfileMixin
connect("test_monitoring")

class MonitoringSettingsFormView(UserProfileMixin, FormView):
    form_class = MonitoringSettingsForm
    template_name = 'user/settings.html'
    success_url = '/user/settings/monitoring/'

    def form_valid(self, form):
        form_data = {}
        for key in form.data.keys():
            form_data[key] = form.data[key]

        print 'form.data: ', form.data
        if form_data['operation'] == 'add_node':
            print 'Add node'
        if form_data['operation'] == 'add_server_group':
            print 'Add group:'
        if form_data['operation'] == 'add_node_to_group':
            print 'Add node to group:'
        if form_data['operation'] == 'del_node_from_group':
            print 'Delete node from group'

        return super(MonitoringSettingsFormView, self).form_valid(form)

    def form_invalid(self, form):
        return self.form_valid(form)