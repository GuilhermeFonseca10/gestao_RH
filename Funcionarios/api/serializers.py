from rest_framework.serializers import ModelSerializer
from Funcionarios.models import Funcionario

class FuncionarioSerializer(ModelSerializer):
    class Meta:
        model = Funcionario
        fields = ('nome', 'user')