from django.contrib import admin
from django.urls import path, include
from .views import FuncionariosList
from .views import FuncionariosEdit
from .views import FuncionariosDelete
from .views import FuncionariosCreate

urlpatterns = [
    path('', FuncionariosList.as_view(), name='list_funcionarios'),
    path('editar/<int:pk>', FuncionariosEdit.as_view(), name='update_funcionarios'),
    path('delete/<int:pk>', FuncionariosDelete.as_view(), name='delete_funcionarios'),
    path('criar/', FuncionariosCreate.as_view(), name='create_funcionarios'),
]
