from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import (
    path, include
)

from . import views

urlpatterns = [
    path('',
         views.HomeView.as_view(), name='home'),

    path('golf/',
         include('golf.urls', namespace='golf')),

    path('help/',
         include('help.urls', namespace='help')),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns = urlpatterns \
                  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
                  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'conf.views.handler404'
handler403 = 'conf.views.handler403'
handler500 = 'conf.views.handler500'
