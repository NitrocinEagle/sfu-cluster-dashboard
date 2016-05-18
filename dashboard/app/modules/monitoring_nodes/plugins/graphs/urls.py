# -*- coding: utf8 -*-
from __future__ import absolute_import
from django.conf.urls import url
from .views import GraphsPluginsView

urlpatterns = [
    url(r'^$', GraphsPluginsView.as_view()),
]