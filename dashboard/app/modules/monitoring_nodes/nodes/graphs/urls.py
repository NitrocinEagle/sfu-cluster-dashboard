# -*- coding: utf8 -*-
from __future__ import absolute_import
from django.conf.urls import url, include
from .views import GraphsNodesView

urlpatterns = [
    url(r'^$', GraphsNodesView.as_view()),
]