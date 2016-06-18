# -*- coding: utf8 -*-
from __future__ import absolute_import
from django.conf.urls import url
from .views import MonitoringInfoGet

urlpatterns = [
    url(r'info/', MonitoringInfoGet.as_view()),
]
