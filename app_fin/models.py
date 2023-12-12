from django.db import models

TIPO_CHOICES = (
    ("E", "Entrada"),
    ("S", "Saida"),
)


# Create your models here.
class db_financeiro(models.Model):
    tbl_movimentacao = models.CharField(max_length=100, verbose_name="Descrição")
    tbl_data = models.DateField(null=False, blank=False, verbose_name="Data")
    tbl_tipo = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        choices=TIPO_CHOICES,
        verbose_name="Tipo",
    )
    tbl_valor = models.FloatField(blank=False, null=False, verbose_name="Valor")
    tbl_data_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Data de Criação"
    )
    tbl_obs = models.TextField(blank=True, null=True, verbose_name="Observação")
