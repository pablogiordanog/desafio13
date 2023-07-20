from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from .views import ListNotice, AddNotice

urlpatterns = [
    path('list/', ListNotice.as_view(), name='list'),
    path("add_notice/", AddNotice.as_view(), name='add_notice'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

