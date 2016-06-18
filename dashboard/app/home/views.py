# -*- coding: utf8 -*-
from __future__ import absolute_import

from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.views.generic import FormView, TemplateView
from django.views.generic.base import View
from ..mongo_models import ServerGeneralInfo, PluginInfo, NodeInfo


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
    template_name = 'site/index/dashboard.html'

    def get_context_data(self, **kwargs):
        kwargs['server_info'] = ServerGeneralInfo.objects()

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
        },]

        kwargs['notifications'] = [{
            'id': 1,
            'type': 'info',
            'text': u'Система оповещений находится в разработке',
            'time': '08:00 20.05.2016',
        }, {
            'id': 1,
            'type': 'critical',
            'text': u'Проверьте узел ULK416-cluster1-0',
            'time': '16:04 21.05.2016',
        }, {
            'id': 1,
            'type': 'critical',
            'text': u'Проверьте узел ULK416-cluster1-1',
            'time': '17:14 22.05.2016',
        }, {
            'id': 2,
            'type': 'config',
            'text': u'Изменен таймаут параметра cpu_percent в узле ULK416-cluster1-0',
            'time': '13:34 26.05.2016',
        }, {
            'id': 3,
            'type': 'info',
            'text': u'Добавлен узел ULK416-cluster1-2',
            'time': '11:39 27.05.2016',
        }, {
            'id': 3,
            'type': 'critical',
            'text': u'Проверьте узел ULK416-cluster1-2',
            'time': '12:43 28.05.2016',
        }, {
            'id': 4,
            'type': 'warning',
            'text': u'Параметр cpu_pecent на узле ULK416-cluster1-2 выше нормы',
            'time': '09:21 29.05.2016',
        },]
        kwargs['plugins'] = PluginInfo.objects()
        kwargs['nodes'] = NodeInfo.objects()
        return super(DashboardView, self).get_context_data(**kwargs)
