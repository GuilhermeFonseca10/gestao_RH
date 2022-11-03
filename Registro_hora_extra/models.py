from django.db import models
from Funcionarios.models import Funcionario

class Registro_hora_extra(models.Model):
    motivo = models.CharField(max_length=100)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.motivo)

# Create your models here.
