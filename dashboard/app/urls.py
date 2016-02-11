from django.conf.urls import url, include

urlpatterns = [
    url(r'^dashboard/', include('app.dashboard.urls')),
    url(r'^plugins/', include('app.plugins.urls')),
    url(r'^nodes/', include('app.nodes.urls')),
    url(r'^api/', include('app.api.urls')),
    url(r'^', include('app.index.urls')),
]
