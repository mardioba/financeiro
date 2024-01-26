# financas/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class Despesa(models.Model):
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()


class Receita(models.Model):
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()

#### LOGIN ####
class CustomUser(AbstractUser):
    # Adicione aqui os campos personalizados que deseja ter no modelo de usuário

    class Meta:
        app_label = "financas"