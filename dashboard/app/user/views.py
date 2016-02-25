# -*- coding: utf8 -*-
from __future__ import absolute_import
from django.shortcuts import render
from django.views.generic import View
from ..mongo_models import PluginInfo, ParamInfo
from mongoengine import connect

connect("test_monitoring")

class UserHomePageView(View):
    pass