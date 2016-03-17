from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^plugins/', include('app.plugins.urls')),
    url(r'^nodes/', include('app.nodes.urls')),
    url(r'^api/', include('app.api.urls')),
    url(r'^user/', include('app.user.urls')),
    url(r'^', include('app.index.urls')),
]
