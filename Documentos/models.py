from django.db import models
from Funcionarios.models import Funcionario

class Documento(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    pertence = models.ForeignKey(Funcionario, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.nome)

# Create your models here.
