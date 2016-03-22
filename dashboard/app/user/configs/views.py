# -*- coding: utf8 -*-
from __future__ import absolute_import
from django.views.generic import TemplateView
from mongoengine import connect

connect("test_monitoring")


class UserSettingView(TemplateView):
    template_name = 'user/settings.html'
