from django.shortcuts import render
from rest_framework import viewsets, permissions
from funcionario.serializers import FuncionarioSerializer

from funcionario.models import Funcionario

# Create your views here.

class FuncionarioViewset(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    permission_classes = [permissions.IsAuthenticated]

