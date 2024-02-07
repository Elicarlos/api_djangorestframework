from rest_framework import serializers

from empresa.models import Empresa


class EmpresaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'