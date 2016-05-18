# -*- coding: utf8 -*-
from __future__ import absolute_import
from django.conf.urls import url, include


urlpatterns = [
    url(r'^monitoring_nodes/', include('app.modules.monitoring_nodes.urls')),
]
