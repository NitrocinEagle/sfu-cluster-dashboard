# -*- coding: utf8 -*-
from __future__ import absolute_import
from django.views.generic import TemplateView
from mongoengine import connect

connect("test_monitoring")

# connect('test', host='192.168.1.106', port=27017)

class ModulesView(TemplateView):
    template_name = 'site/modules/index.html'