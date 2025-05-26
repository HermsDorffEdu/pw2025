from django.urls import path
from .views import (
    Inicio,
    ClienteCreate, ClienteUpdate, 
    FotografoCreate, FotografoUpdate,
    EstudioCreate, EstudioUpdate,
    SessaoFotoCreate, SessaoFotoUpdate,
)

urlpatterns = [
    path("", Inicio.as_view(), name="inicio"),

    path("adicionar/cliente/", ClienteCreate.as_view(), name="inserir-cliente"),
    path("adicionar/fotografo/", FotografoCreate.as_view(), name="inserir-fotografo"),
    path("adicionar/estudio/", EstudioCreate.as_view(), name="inserir-estudio"),
    path("adicionar/sessao/", SessaoFotoCreate.as_view(), name="inserir-sessao"),

    path("editar/cliente/<int:pk>/", ClienteUpdate.as_view(), name="editar-cliente"),
    path("editar/fotografo/<int:pk>/", FotografoUpdate.as_view(), name="editar-fotografo"),
    path("editar/estudio/<int:pk>/", EstudioUpdate.as_view(), name="editar-estudio"),
    path("editar/sessao/<int:pk>/", SessaoFotoUpdate.as_view(), name="editar-sessao"),

]
