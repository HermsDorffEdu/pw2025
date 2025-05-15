from django.urls import path
from .views import (
    Inicio,
    ClienteCreate,
    FotografoCreate,
    EstudioCreate,
    SessaoFotoCreate
)

urlpatterns = [
    path("", Inicio.as_view(), name="inicio"),
    path("adicionar/cliente/<int:pk/", ClienteCreate.as_view(), name="inserir-cliente"),
    path("adicionar/fotografo/<int:pk/", FotografoCreate.as_view(), name="inserir-fotografo"),
    path("adicionar/estudio/<int:pk/", EstudioCreate.as_view(), name="inserir-estudio"),
    path("adicionar/sessao/<int:pk/", SessaoFotoCreate.as_view(), name="inserir-sessao"),
]
