from django.db import models
from django.urls import reverse

from apps.funcionarios.models import Funcionario


class Documento(models.Model):
    descricao = models.CharField(max_length=100, null=True, blank=True)
    pertence = models.ForeignKey(Funcionario, on_delete=models.PROTECT, null=True, blank=True)
    arquivo = models.FileField(upload_to='documentos', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('update_funcionarios', args=[self.pertence.id])

    def __str__(self):
        return self.descricao
