from django.db import models

# Create your models here.
class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=100)
    rg = models.CharField(max_length=100)
    pis = models.CharField(max_length=100)
    foto = models.IntegerField()

    def __str__(self):
        return self.nome