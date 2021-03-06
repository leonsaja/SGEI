
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='core')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('accounts/', include('allauth.urls')),
    path('editais/', include('editais.urls', namespace='editais')),
    path('relatorios/', include('relatorios.urls', namespace='relatorios')),





]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)\
      + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.AdminSite.site_header='Sistema de Gereciamento'