# -*- coding: utf8 -*-
from __future__ import absolute_import

from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.views.generic import FormView, TemplateView
from django.views.generic.base import View
from ..mongo_models import ServerInfo, PluginInfo, NodeInfo
from .forms import SimpleForm


# login 'test' password 'test1234'
class LoginFormView(FormView):
    form_class = AuthenticationForm

    template_name = "index/login.html"
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
    template_name = 'index/dashboard.html'

    def get_context_data(self, **kwargs):
        kwargs['server_info'] = ServerInfo.objects.first().info
        kwargs['plugins'] = PluginInfo.objects()
        kwargs['nodes'] = NodeInfo.objects()
        return super(DashboardView, self).get_context_data(**kwargs)


class SimpleFormView(FormView):
    form_class = SimpleForm
    template_name = 'index/simpleform.html'

    def form_valid(self, form):
        print form.data
        return HttpResponseRedirect('/')

    def form_invalid(self, form):
        print form.data
        return HttpResponseRedirect('/')
