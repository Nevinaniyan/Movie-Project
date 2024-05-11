
from django.contrib import admin
from django.urls import path
from movies import views
from django.conf import settings                       # to display media content
from django.conf.urls.static import static             # to display media content
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('movies.urls'),name="home"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)        # to display media content
