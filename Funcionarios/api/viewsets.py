from rest_framework.viewsets import ModelViewSet
from Funcionarios.api.serializers import FuncionarioSerializer
from Funcionarios.models import Funcionario


class FuncionarioViewSet(ModelViewSet):

    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer

