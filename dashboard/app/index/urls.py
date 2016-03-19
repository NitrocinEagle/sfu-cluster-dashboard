# -*- coding: utf8 -*-
from __future__ import absolute_import
from django.conf.urls import url
from .views import LoginFormView, LogoutView, DashboardView, SimpleFormView

urlpatterns = [
    url(r'^login/$', LoginFormView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^$', DashboardView.as_view(), name='dashboard'),

    url(r'^simple_form/$', SimpleFormView.as_view()),
]
