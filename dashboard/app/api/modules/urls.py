# -*- coding: utf8 -*-
from __future__ import absolute_import
from django.conf.urls import url, include

urlpatterns = [
    url(r'monitoring-nodes/', include('app.api.modules.monitoring_nodes.urls', namespace='monitoring_nodes')),
]