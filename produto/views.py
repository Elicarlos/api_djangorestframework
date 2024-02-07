from django.shortcuts import render
from rest_framework import permissions, viewsets
from .serializers import ProdutoSerializer
from . models import Produto

# Create your views here.

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    permission_classes = [permissions.IsAuthenticated]
