from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import Funcionario


class FuncionariosList(ListView):
    model = Funcionario

    def get_queryset(self):
        print(self.request.user)
        empresa_logada = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa_logada)


class FuncionariosEdit(UpdateView):
    model = Funcionario
    fields = ['nome', 'departamentos']


class FuncionariosDelete(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('list_funcionarios')


class PegaUser:
    def __init__(self):
        self.pega = ''


class FuncionariosCreate(CreateView):
    model = Funcionario
    fields = ['nome', 'departamentos']

    def form_valid(self, form):
        funcionario = form.save(commit=False) # salva na memoria e nao no BD
        username = funcionario.nome.split(' ')[0] +'at'+funcionario.nome.split(' ')[1]
        print('username: ', username)
        funcionario.empresa = self.request.user.funcionario.empresa
        print('funcionario.empresa = ', funcionario.empresa)
        funcionario.user = User.objects.create(username=username)
        print('funcionario.user = ', funcionario.user)
        funcionario.user = self.request.user
        print('funcionario.user apos self.request = ', funcionario.user)
        funcionario.save()
        return super(FuncionariosCreate, self).form_valid(form)
#             return redirect('list_funcionarios')

