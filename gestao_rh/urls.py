from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from apps.funcionarios import urls as funcionarios_urls
from apps.departamentos import urls as departamentos_urls
from apps.core import urls as core_urls
from apps.empresas import urls as empresas_urls
from apps.documentos import urls as documentos_urls
from apps.registro_hora_extra import urls as registro_horas_extras_urls

urlpatterns = [
    path('', include(core_urls)),
    path('funcionarios/', include(funcionarios_urls)),
    path('departamentos/', include(departamentos_urls)),
    path('empresas/', include(empresas_urls)),
    path('documentos/', include(documentos_urls)),
    path('horas_extras/', include(registro_horas_extras_urls)),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
