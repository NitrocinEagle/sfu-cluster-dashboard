# -*- coding: utf8 -*-
from __future__ import absolute_import
from django.conf.urls import url
from .views import MonitoringSettingsFormView

urlpatterns = [
    url(r'^$', MonitoringSettingsFormView.as_view(), name='index'),
]