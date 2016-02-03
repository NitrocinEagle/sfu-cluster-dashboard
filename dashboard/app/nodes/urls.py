__author__ = 'mist'
from django.conf.urls import url
from views import NodesView

urlpatterns = [
    url(r'^$', NodesView.as_view()),
]