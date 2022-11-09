from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Funcionario

class FuncionariosList(ListView):
    model = Funcionario

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa_logada)

# Create your views here.
