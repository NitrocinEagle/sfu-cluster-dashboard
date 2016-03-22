# -*- coding: utf8 -*-
from __future__ import absolute_import
from django.conf.urls import url
from .views import UserSettingView

urlpatterns = [
    url(r'^$', UserSettingView.as_view()),
    url(r'^preview/$', UserSettingView.as_view()),
    url(r'^change_password/', UserSettingView.as_view()),
]