# -*- coding: utf8 -*-
from __future__ import absolute_import
from django.conf.urls import url, include
from .views import ModulesView


urlpatterns = [
    url(r'^$', ModulesView.as_view(), name='index'),
    url(r'^monitoring_nodes/', include('app.modules.monitoring_nodes.urls', namespace='monitoring_nodes')),
]
