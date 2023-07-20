from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views import index, acerca_de

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name='index'),
    path('noticias/', include('apps.noticias.urls')),
    path('categorias/', include('apps.categorias.urls')),
    path('acerca_de/', acerca_de, name='acerca_de'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
