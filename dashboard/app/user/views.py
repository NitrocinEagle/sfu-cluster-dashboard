# -*- coding: utf8 -*-
from django.views.generic import TemplateView
from mixins import UserProfileMixin


class UserProfileView(UserProfileMixin, TemplateView):
    template_name = 'site/user/profile.html'
