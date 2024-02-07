from django.db import models

# Create your models here.
class Empresa(models.Model):
    cnpj = models.CharField(max_length=100)
    fantasia = models.CharField(max_length=100)
    razao_social = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    logo = models.ImageField()

    def __str__(self) -> str:
        return self.fantasia
    