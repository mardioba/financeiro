# financas/views.py
from django.utils import translation
from django.shortcuts import render, redirect, get_object_or_404
from .models import Despesa, Receita
from .forms import DespesaForm, ReceitaForm
from django.views.generic import View
from django.db.models import Sum
from datetime import datetime, date
import locale
import calendar


def adicionar_despesa(request):
    if request.method == "POST":
        form = DespesaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listar_despesas")
    else:
        form = DespesaForm()
    return render(request, "financas/adicionar_despesa.html", {"form": form})


def adicionar_receita(request):
    if request.method == "POST":
        form = ReceitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listar_receitas")
    else:
        form = ReceitaForm()
    return render(request, "financas/adicionar_receita.html", {"form": form})


def relatorio_atual(request):
    hoje = date.today()
    primeiro_dia_do_mes = hoje.replace(day=1)
    ultimo_dia_do_mes = hoje.replace(day=28)  # Adapte conforme necessário
    mes = hoje.month
    despesas_mes = Despesa.objects.filter(
        data__range=[primeiro_dia_do_mes, ultimo_dia_do_mes]
    )
    receitas_mes = Receita.objects.filter(
        data__range=[primeiro_dia_do_mes, ultimo_dia_do_mes]
    )
    locale.setlocale(locale.LC_TIME, "pt_BR.UTF-8")
    nome_mes = calendar.month_name[int(mes)]
    total_despesas = despesas_mes.aggregate(Sum("valor"))["valor__sum"] or 0
    total_receitas = receitas_mes.aggregate(Sum("valor"))["valor__sum"] or 0

    saldo_mes = total_receitas - total_despesas

    return render(
        request,
        "financas/relatorio.html",
        {
            "despesas_mes": despesas_mes,
            "receitas_mes": receitas_mes,
            "total_despesas": total_despesas,
            "total_receitas": total_receitas,
            "saldo_mes": saldo_mes,
            "nmes": nome_mes,
        },
    )


def relatorio(request, ano, mes):
    primeiro_dia_do_mes = date(int(ano), int(mes), 1)
    ultimo_dia_do_mes = primeiro_dia_do_mes.replace(
        day=28
    )  # Adapte conforme necessário

    despesas_mes = Despesa.objects.filter(
        data__range=[primeiro_dia_do_mes, ultimo_dia_do_mes]
    )
    receitas_mes = Receita.objects.filter(
        data__range=[primeiro_dia_do_mes, ultimo_dia_do_mes]
    )
    locale.setlocale(locale.LC_TIME, "pt_BR.UTF-8")
    nome_mes = calendar.month_name[int(mes)]
    total_despesas = despesas_mes.aggregate(Sum("valor"))["valor__sum"] or 0
    total_receitas = receitas_mes.aggregate(Sum("valor"))["valor__sum"] or 0

    saldo_mes = total_receitas - total_despesas

    return render(
        request,
        "financas/relatorio.html",
        {
            "despesas_mes": despesas_mes,
            "receitas_mes": receitas_mes,
            "total_despesas": total_despesas,
            "total_receitas": total_receitas,
            "saldo_mes": saldo_mes,
            "nmes": nome_mes,
        },
    )


def home(request):
    return render(request, "financas/home.html")


def selecionar_mes_ano(request):
    anos = range(datetime.now().year, 2000, -1)
    meses = [
        (str(month), datetime.strptime(str(month), "%m").strftime("%B"))
        for month in range(1, 13)
    ]
    locale.setlocale(locale.LC_TIME, "pt_BR.UTF-8")
    selected_year = request.GET.get("ano", datetime.now().year)
    selected_month = request.GET.get("mes", datetime.now().month)

    return render(
        request,
        "financas/selecionar_mes_ano.html",
        {
            "anos": anos,
            "meses": meses,
            "selected_year": selected_year,
            "selected_month": selected_month,
        },
    )


def selecionar_ano(request):
    translation.activate("pt_BR")
    anos = range(datetime.now().year, 2000, -1)
    locale.setlocale(locale.LC_TIME, "pt_BR.UTF-8")
    selected_year = request.GET.get("ano", datetime.now().year)

    return render(
        request,
        "financas/selecionar_ano.html",
        {
            "anos": anos,
            "selected_year": selected_year,
        },
    )


def despesas_mes_ano(request):
    anos = range(datetime.now().year, 2000, -1)
    meses = [
        (str(month), datetime.strptime(str(month), "%m").strftime("%B"))
        for month in range(1, 13)
    ]
    locale.setlocale(locale.LC_TIME, "pt_BR.UTF-8")
    selected_year = request.GET.get("ano", datetime.now().year)
    selected_month = request.GET.get("mes", datetime.now().month)

    return render(
        request,
        "financas/despesas_mes_ano.html",
        {
            "anos": anos,
            "meses": meses,
            "selected_year": selected_year,
            "selected_month": selected_month,
        },
    )


def receitas_mes_ano(request):
    anos = range(datetime.now().year, 2000, -1)
    meses = [
        (str(month), datetime.strptime(str(month), "%m").strftime("%B"))
        for month in range(1, 13)
    ]
    locale.setlocale(locale.LC_TIME, "pt_BR.UTF-8")
    selected_year = request.GET.get("ano", datetime.now().year)
    selected_month = request.GET.get("mes", datetime.now().month)

    return render(
        request,
        "financas/receitas_mes_ano.html",
        {
            "anos": anos,
            "meses": meses,
            "selected_year": selected_year,
            "selected_month": selected_month,
        },
    )


def pesquisa_despesas(request, ano, mes):
    primeiro_dia_do_mes = date(int(ano), int(mes), 1)
    ultimo_dia_do_mes = primeiro_dia_do_mes.replace(
        day=28
    )  # Adapte conforme necessário

    despesas_mes = Despesa.objects.filter(
        data__range=[primeiro_dia_do_mes, ultimo_dia_do_mes]
    )
    locale.setlocale(locale.LC_TIME, "pt_BR.utf-8")
    nome_mes = calendar.month_name[int(mes)]
    return render(
        request,
        "financas/despesas_mes_RESULT.html",
        {
            "despesas_mes": despesas_mes,
        },
    )


def pesquisa_receitas(request, ano, mes):
    primeiro_dia_do_mes = date(int(ano), int(mes), 1)
    ultimo_dia_do_mes = primeiro_dia_do_mes.replace(
        day=28
    )  # Adapte conforme necessário

    receitas_mes = Receita.objects.filter(
        data__range=[primeiro_dia_do_mes, ultimo_dia_do_mes]
    )
    locale.setlocale(locale.LC_TIME, "pt_BR.utf-8")
    nome_mes = calendar.month_name[int(mes)]
    print(nome_mes)
    return render(
        request,
        "financas/receitas_mes_RESULT.html",
        {
            "receitas_mes": receitas_mes,
            "nome_mes": nome_mes,
            "ano": ano,
            "nmes": mes,
        },
    )


# Aqui
def relatorio_ano(request, ano):
    relatorio_anual = []

    for mes in range(1, 13):
        primeiro_dia_do_mes = date(int(ano), mes, 1)
        ultimo_dia_do_mes = primeiro_dia_do_mes.replace(day=28)

        receitas_mes = (
            Receita.objects.filter(
                data__range=[primeiro_dia_do_mes, ultimo_dia_do_mes]
            ).aggregate(total_receitas_mes=Sum("valor"))["total_receitas_mes"]
            or 0
        )

        despesas_mes = (
            Despesa.objects.filter(
                data__range=[primeiro_dia_do_mes, ultimo_dia_do_mes]
            ).aggregate(total_despesas_mes=Sum("valor"))["total_despesas_mes"]
            or 0
        )

        saldo_mes = receitas_mes - despesas_mes

        nome_mes = calendar.month_name[mes]

        relatorio_mes = {
            "nome_mes": nome_mes,
            "ano": ano,
            "nmes": mes,
            "receitas_mes": receitas_mes,
            "despesas_mes": despesas_mes,
            "saldo_mes": saldo_mes,
        }

        relatorio_anual.append(relatorio_mes)

    saldo_anual = sum(relatorio["saldo_mes"] for relatorio in relatorio_anual)

    return render(
        request,
        "financas/relatorio_ano.html",
        {"relatorio_anual": relatorio_anual, "ano": ano, "saldo_anual": saldo_anual},
    )


class FaviconView(View):
    def get(self, request, *args, **kwargs):
        # Pode ser necessário ajustar o caminho para o seu favicon
        return redirect("/static/favicon.ico")


######## EDITAR REGISTROS ###################################################
def editar_receita(request, receita_id):
    receita = get_object_or_404(Receita, id=receita_id)
    if request.method == "POST":
        form = ReceitaForm(request.POST, instance=receita)
        if form.is_valid():
            form.save()
            return redirect("todas_receitas")
    else:
        form = ReceitaForm(instance=receita)

    return render(
        request, "financas/editar_receita.html", {"form": form, "receita": receita}
    )


def editar_despesa(request, despesa_id):
    despesa = get_object_or_404(Despesa, id=despesa_id)
    if request.method == "POST":
        form = DespesaForm(request.POST, instance=despesa)
        if form.is_valid():
            form.save()
            return redirect("todas_despesas")
    else:
        form = DespesaForm(instance=despesa)

    return render(
        request, "financas/editar_despesa.html", {"form": form, "despesa": despesa}
    )


def todas_despesas(request):
    todas_despesas = Despesa.objects.all()
    return render(request, "financas/todas_despesas.html", {"despesas": todas_despesas})


def todas_receitas(request):
    todas_receitas = Receita.objects.all()
    return render(request, "financas/todas_receitas.html", {"receitas": todas_receitas})


###### EXCLUIR REGISTROS ##################################################
def excluir_receita(request, receita_id):
    receita = get_object_or_404(Receita, id=receita_id)
    if request.method == "POST":
        receita.delete()
        return redirect("todas_receitas")

    return render(request, "financas/excluir_receita.html", {"receita": receita})


def excluir_despesa(request, despesa_id):
    despesa = get_object_or_404(Despesa, id=despesa_id)
    if request.method == "POST":
        despesa.delete()
        return redirect("todas_despesas")

    return render(request, "financas/excluir_despesa.html", {"despesa": despesa})
