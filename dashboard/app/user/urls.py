# -*- coding: utf8 -*-
from django.conf.urls import url, include
from views import UserProfileView

urlpatterns = [
    url(r'^$', UserProfileView.as_view()),
    url(r'^profile/$', UserProfileView.as_view(), name='profile'),
    url(r'^settings/', include('app.user.configs.urls', namespace='settings')),
]