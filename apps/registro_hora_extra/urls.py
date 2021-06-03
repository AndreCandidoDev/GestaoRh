from django.contrib import admin
from django.urls import path, include
from .views import ListHoras
from .views import EditHoras
from .views import CreateHoras
from .views import DeleteHoras

urlpatterns = [
    path('', ListHoras.as_view(), name='list_horas'),
    path('novo/', CreateHoras.as_view(), name='create_horas'),
    path('edit/<int:pk>', EditHoras.as_view(), name='edit_horas'),
    path('delete/<int:pk>', DeleteHoras.as_view(), name='delete_horas'),
]