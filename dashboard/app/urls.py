from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^plugins/', include('app.plugins.urls', namespace='index')),
    url(r'^nodes/', include('app.nodes.urls', namespace='nodes')),
    url(r'^api/', include('app.api.urls', namespace='api')),
    url(r'^user/', include('app.user.urls', namespace='user')),
    url(r'^', include('app.index.urls', namespace='index')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
