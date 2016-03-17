# -*- coding: utf8 -*-
from __future__ import absolute_import

from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.views.generic import FormView, TemplateView
from django.views.generic.base import View
from ..mongo_models import ServerInfo
from .forms import SimpleForm


class LoginFormView(FormView):
    # login 'test' password 'test1234'
    form_class = AuthenticationForm

    template_name = "index/index.html"
    success_url = "/dashboard"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")


class DashboardView(TemplateView):
    template_name = 'index/dashboard.html'

    def get_context_data(self, **kwargs):
        kwargs['server_info'] = ServerInfo.objects.first()
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