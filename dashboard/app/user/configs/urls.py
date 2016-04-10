# -*- coding: utf8 -*-
from __future__ import absolute_import
from django.conf.urls import url
from .views import MonitoringSettingsFormView

urlpatterns = [
    url(r'^user/', MonitoringSettingsFormView.as_view(), name='user'),
    url(r'^monitoring/', MonitoringSettingsFormView.as_view(), name='monitoring'),
    url(r'^dashboard/', MonitoringSettingsFormView.as_view(), name='dashboard'),
]