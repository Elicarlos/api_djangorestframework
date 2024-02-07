from django.db import models

# Create your models here.

class Produto(models.Model):
    codigo = models.IntegerField()
    codigo_barras = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.descricao