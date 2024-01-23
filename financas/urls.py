# financas/urls.py
from django.urls import path
from .views import (
    adicionar_despesa,
    adicionar_receita,
    relatorio,
    relatorio_atual,
    selecionar_mes_ano,
    receitas_mes_ano,
    despesas_mes_ano,
    pesquisa_despesas,
    pesquisa_receitas,
    relatorio_ano,
    selecionar_ano,
)

urlpatterns = [
    path("despesas/", despesas_mes_ano, name="listar_despesas"),
    path("receitas/", receitas_mes_ano, name="listar_receitas"),
    path("adicionar_despesa/", adicionar_despesa, name="adicionar_despesa"),
    path("adicionar_receita/", adicionar_receita, name="adicionar_receita"),
    path("relatorio/", relatorio_atual, name="relatorio_atual"),  # Adicione esta linha
    path(
        "relatorio/<int:ano>/<int:mes>/", relatorio, name="relatorio"
    ),  # Adicione esta linha
    path("selecionar_mes_ano/", selecionar_mes_ano, name="selecionar_mes_ano"),
    path(
        "p_despesas/<int:ano>/<int:mes>/", pesquisa_despesas, name="pesquisa_despesas"
    ),  # Adicione esta linha
    path(
        "p_receitas/<int:ano>/<int:mes>/", pesquisa_receitas, name="pesquisa_receitas"
    ),  # Adicione esta linha
    path("relatorio_ano/<int:ano>/", relatorio_ano, name="relatorio_ano"),
    path("selecionar_ano/", selecionar_ano, name="selecionar_ano"),
]
