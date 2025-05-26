from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Cliente, Fotografo, Estudio, SessaoFoto

class Inicio(TemplateView):
    template_name = "paginas/index.html"

class ClienteCreate(CreateView):
    model = Cliente
    fields = ['nome', 'telefone', 'email']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('inicio')
    extra_content = {'Cadastro Fotografia': 'Atualização de fotos', 'Enviar dados': 'protocolar',}
    

class FotografoCreate(CreateView):
    model = Fotografo
    fields = ['nome', 'especialidade', 'telefone']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('inicio')
    extra_content = {'Cadastro Fotografia': 'Atualização de fotos', 'Enviar dados': 'protocolar',}

class EstudioCreate(CreateView):
    model = Estudio
    fields = ['nome', 'endereco', 'telefone']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('inicio')
    extra_content = {'Cadastro Fotografia': 'Atualização de fotos', 'Enviar dados': 'protocolar',}

class SessaoFotoCreate(CreateView):
    model = SessaoFoto
    fields = ['data', 'horario', 'tipo', 'duracao', 'cliente', 'fotografo', 'estudio']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('inicio')
    extra_content = {'Cadastro Fotografia': 'Atualização de fotos', 'Enviar dados': 'protocolar',}

