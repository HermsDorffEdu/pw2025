
from .views import CampusCreate, CursoCreate
from django.urls import path
from .views import Inicio
urlpatterns = [
    path("index/", Inicio.as_view(), name = "inicio"),
    path("form/", form.as_view(), name = "form"),
    path("Adicionar/campus/", CampusCreate.as_view(), name ="inserir-campus"),
    path("Adicionar/curso/", CursoCreate.as_view(), name ="inserir-curso"),
]
