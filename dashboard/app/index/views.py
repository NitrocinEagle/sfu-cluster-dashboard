# -*- coding: utf8 -*-
from __future__ import absolute_import
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import FormView
from django.views.generic.base import View


class LoginFormView(FormView):
    # login 'test' password 'test1234'
    form_class = AuthenticationForm

    template_name = "index/login.html"
    success_url = "/dashboard"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")


class IndexView(View):
    template_name = 'index/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
