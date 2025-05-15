from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()

class Fotografo(models.Model):
    nome = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)

class Estudio(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)

class SessaoFoto(models.Model):
    data = models.DateField()
    horario = models.TimeField()
    tipo = models.CharField(max_length=50)
    duracao = models.PositiveIntegerField()

    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    fotografo = models.ForeignKey(Fotografo, on_delete=models.PROTECT)
    estudio = models.ForeignKey(Estudio, on_delete=models.PROTECT)
