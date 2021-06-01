from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from .models import Empresa

# Create your views here.


class EmpresaCreate(CreateView):
    model = Empresa
    fields = ['nome']

    def form_valid(self, form):
        obj = form.save()  # recebe o form
        funcionario = self.request.user.funcionario  # pega o funcionario
        funcionario.empresa = obj  # campo empresa recebe obj
        funcionario.save()  # salva no BD
        return HttpResponse('ok')


class EmpresaEdit(UpdateView):
    model = Empresa
    fields = ['nome']
