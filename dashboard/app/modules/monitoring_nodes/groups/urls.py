# -*- coding: utf8 -*-
from __future__ import absolute_import
from django.conf.urls import url
from .views import GroupsView

urlpatterns = [
    url(r'^$', GroupsView.as_view(), name='index'),
]
