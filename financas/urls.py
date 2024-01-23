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
    editar_despesa,
    editar_receita,
    todas_despesas,
    todas_receitas,
    excluir_despesa,
    excluir_receita,
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
    path("editar_receita/<int:receita_id>/", editar_receita, name="editar_receita"),
    path("editar_despesa/<int:despesa_id>/", editar_despesa, name="editar_despesa"),
    path("todas_despesas/", todas_despesas, name="todas_despesas"),
    path("todas_receitas/", todas_receitas, name="todas_receitas"),
    path("excluir_receita/<int:receita_id>/", excluir_receita, name="excluir_receita"),
    path("excluir_despesa/<int:despesa_id>/", excluir_despesa, name="excluir_despesa"),
]
