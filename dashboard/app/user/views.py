# -*- coding: utf8 -*-
from __future__ import absolute_import

from django.views.generic import View
from mongoengine import connect

connect("test_monitoring")

class UserHomePageView(View):
    pass