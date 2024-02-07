from rest_framework import serializers
from funcionario.models import Funcionario

class FuncionarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Funcionario
        fields = '__all__'
