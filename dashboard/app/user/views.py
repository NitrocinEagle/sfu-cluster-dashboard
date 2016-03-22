# -*- coding: utf8 -*-
from django.views.generic import TemplateView
from app.user.models import UserProfile


class UserProfileView(TemplateView):
    template_name = 'user/profile.html'

    def get_context_data(self, **kwargs):
        kwargs['user_profile'] = UserProfile.objects.get(user=self.request.user)
        return super(UserProfileView, self).get_context_data(**kwargs)
