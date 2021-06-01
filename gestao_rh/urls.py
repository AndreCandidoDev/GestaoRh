from django.contrib import admin
from django.urls import path, include
from apps.funcionarios import urls as funcionarios_urls
from apps.departamentos import urls as departamentos_urls
from apps.core import urls as core_urls
from apps.empresas import urls as empresas_urls

urlpatterns = [
    path('', include(core_urls)),
    path('funcionarios/', include(funcionarios_urls)),
    path('departamentos/', include(departamentos_urls)),
    path('empresas/', include(empresas_urls)),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]
