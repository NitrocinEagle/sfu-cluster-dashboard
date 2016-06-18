from app.user.models import UserProfile


class UserProfileMixin(object):
    def get_context_data(self, **kwargs):
        kwargs['user_profile'] = UserProfile.objects.get(user=self.request.user)
        return super(UserProfileMixin, self).get_context_data(**kwargs)
