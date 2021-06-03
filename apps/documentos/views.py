from django.shortcuts import render
from django.views.generic import CreateView, DeleteView
from .models import Documento


class CreateDocumento(CreateView):
    model = Documento
    fields = ['descricao', 'pertence', 'arquivo']

    # def post(self, request, *args, **kwargs):  # não funciona
    #     form = self.get_form()
    #     form.instance.pertence_id = self.kwargs['funcionarios_id']
    #     if form.is_valid():
    #         return self.form_valid(form)
    #     else:
    #         return self.form_invalid(form)


class DeleteDocumento(DeleteView):
    pass