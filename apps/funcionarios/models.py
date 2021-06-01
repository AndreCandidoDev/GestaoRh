from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from apps.departamentos.models import Departamento
from apps.empresas.models import Empresa


class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    User = models.OneToOneField(User, on_delete=models.PROTECT, null=True, blank=True)
    departamentos = models.ManyToManyField(Departamento)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('list_funcionarios')

    def __str__(self):
        return self.nome

#  por ser um sistema de gestão, a empresa deve requisitar uma chave
#  de autenticação e apartir desse usuario elaborar as operações no sistema

