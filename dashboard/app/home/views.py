# -*- coding: utf8 -*-
from __future__ import absolute_import

from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.views.generic import FormView, TemplateView
from django.views.generic.base import View
from ..mongo_models import ServerInfo, PluginInfo, NodeInfo


# login 'test' password 'test1234'
class LoginFormView(FormView):
    form_class = AuthenticationForm

    template_name = "site/index/login.html"
    success_url = "/"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/login")


class DashboardView(TemplateView):
    # template_name = 'index/dashboard.html'
    template_name = 'site/index/new_dashboard.html'

    def get_context_data(self, **kwargs):
        # kwargs['server_info'] = ServerInfo.objects.first().info
        kwargs['server_info'] = [{
            'name': 'name',
            'value': '11',
            'fa_icon': 'fa-gear',
            'label': 'label'
        }, {
            'name': 'name',
            'value': '11',
            'fa_icon': 'fa-gear',
            'label': 'label'
        }, {
            'name': 'name',
            'value': '11',
            'fa_icon': 'fa-gear',
            'label': 'label'
        }, {
            'name': 'name',
            'value': '11',
            'fa_icon': 'fa-gear',
            'label': 'label'
        }]

        kwargs['monitoring_states'] = [{
            'label': '2',
            'fa_icon': 'fa-server',
            'name': u'Мониторинг серверов',
            'url': '/',
            'value': u'Danger'
        }, {
            'label': '2',
            'fa_icon': 'fa-users',
            'name': u'Мониторинг пользователей',
            'url': '/',
            'value': u'Normal'
        }, {
            'label': '2',
            'fa_icon': 'fa-gear',
            'name': u'Мониторинг инженерных параметров',
            'url': '/',
            'value': u'Warning'
        },
        ]
        kwargs['notifications'] = [{
            'id': 1,
            'type': 'critical',
            'text': u'Случилось что-то страшное',
            'time': '12:43 12.09.2016',
        }, {
            'id': 1,
            'type': 'critical',
            'text': u'Случилось что-то страшное',
            'time': '12:43 12.09.2016',
        }, {
            'id': 1,
            'type': 'critical',
            'text': u'Случилось что-то страшное',
            'time': '12:43 12.09.2016',
        }, {
            'id': 2,
            'type': 'config',
            'text': u'Изменен таймаут параметра А в узле Б',
            'time': '12:43 12.09.2016',
        }, {
            'id': 3,
            'type': 'info',
            'text': u'Добавлен узел С',
            'time': '12:43 12.09.2016',
        }, {
            'id': 3,
            'type': 'critical',
            'text': u'Случилось что-то страшное',
            'time': '12:43 12.09.2016',
        }, {
            'id': 4,
            'type': 'warning',
            'text': u'Параметр В выше нормы',
            'time': '12:43 12.09.2016',
        },
        ]
        kwargs['plugins'] = PluginInfo.objects()
        kwargs['nodes'] = NodeInfo.objects()
        return super(DashboardView, self).get_context_data(**kwargs)
