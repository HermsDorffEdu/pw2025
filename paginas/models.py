from django.db import models

# Todas as classes DEVEM herdar de models.Model
class Campus(models.Model):
    nome = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.nome}" 
        
    

class Curso(models.Model):
    nome = models.CharField(max_length=150)
    campus = models.ForeignKey(Campus, on_delete=models.PROTECT)

class TipoSolicitacao(models.Model):
    descricao = models.CharField(max_length=200)
    prazo_externo = models.CharField(max_length=250)
    prazo_externo_dias = models.PositiveSmallIntegerField(default=0)
    prazo_interno = models.CharField(max_length=250)
    prazo_interno_dias = models.PositiveSmallIntegerField(default=0)
    concluido = models.BooleanField(default=False)
