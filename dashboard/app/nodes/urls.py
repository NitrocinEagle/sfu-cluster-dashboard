__author__ = 'mist'
from django.conf.urls import url, include
from views import NodesView

urlpatterns = [
    url(r'^$', NodesView.as_view()),
    url(r'^(?P<node_name>\w+)/graphs/', include('app.nodes.graphs.urls')),
]