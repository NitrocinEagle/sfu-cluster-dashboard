# -*- coding: utf8 -*-
from __future__ import absolute_import
from django.conf.urls import url, include
from .views import UserHomePageView

urlpatterns = [
    url(r'^$', UserHomePageView.as_view()),
    url(r'^profile/$', UserHomePageView.as_view()),
    url(r'^change_password/$', UserHomePageView.as_view()),
    url(r'^previews/$', UserHomePageView.as_view()),
    url(r'^settings/$', UserHomePageView.as_view()),
]