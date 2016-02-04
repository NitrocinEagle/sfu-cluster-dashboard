__author__ = 'mist'
from django.conf.urls import url
from views import GraphsView

urlpatterns = [
    url(r'^$', GraphsView.as_view()),
]