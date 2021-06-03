from django.contrib import admin
from django.urls import path, include
from .views import CreateDocumento
from .views import DeleteDocumento

urlpatterns = [
    # path('new/<int:funcionarios_id/>', CreateDocumento.as_view(), name='create_documento'),
    path('new/', CreateDocumento.as_view(), name='create_documento'),
    # path('delete/<int:pk>', DeleteDocumento.as_view(), name='delete_documento'),
]