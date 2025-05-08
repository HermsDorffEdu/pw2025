from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from.models import Campus, Curso, TipoSolicitacao
from django.urls import reverse_lazy


class Inicio(TemplateView):
    template_name = "paginas/index.html"
    
class FormView(TemplateView):
    template_name = "paginas/form.html"

class CampusCreate(CreateView):
    template_name = 'paginas/form.html'
    model = Campus
    fields = ['nome']
    success_url = reverse_lazy('inicio')
    extra_content = {'titulo' : 'Cadastro de Campus'}

class CursoCreate(CreateView):
    template_name = 'paginas/form.html'
    model = Curso
    fields = [ 'nome', 'campus']
    success_url = reverse_lazy('form')
    extra_context = {'titulo' : 'Cadastro de Curso'}