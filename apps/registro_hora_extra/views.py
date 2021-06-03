from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import RegistroHoraExtra
from .forms import RegistroHoraExtraForm


class ListHoras(ListView):
    model = RegistroHoraExtra

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return RegistroHoraExtra.objects.filter(funcionario__empresa=empresa_logada)


class EditHoras(UpdateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):  # filtra os funcionarios pela empresa do usuario logado
        kwargs = super(EditHoras, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class DeleteHoras(DeleteView):
    model = RegistroHoraExtra
    success_url = reverse_lazy('list_horas')


class CreateHoras(CreateView):
    model = RegistroHoraExtra
    # fields = ['motivo', 'funcionario', 'horas']
    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):
        kwargs = super(CreateHoras, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs
