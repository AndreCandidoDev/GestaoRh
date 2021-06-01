from django.contrib import admin
from django.urls import path, include
from .views import ListDepartamentos
from .views import CreateDepartamentos
from .views import UpdateDepartamentos
from .views import DeleteDepartamentos

urlpatterns = [
    path('list/', ListDepartamentos.as_view(), name='list_departamentos'),
    path('novo/', CreateDepartamentos.as_view(), name='create_departamentos'),
    path('update/<int:pk>', UpdateDepartamentos.as_view(), name='update_departamento'),
    path('delete/<int:pk>', DeleteDepartamentos.as_view(), name='delete_departamento'),
]