# -*- coding: utf8 -*-
from __future__ import absolute_import
from django.conf.urls import url
from .views import MonitoringInfoView

urlpatterns = [
    url(r'^$', MonitoringInfoView.as_view(), name='index'),
]
