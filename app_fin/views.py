from django.shortcuts import render, redirect
from app_fin.models import db_financeiro
from django.views.generic import ListView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.db.models import Sum
from .forms import MovimentecaoForm


def home(request):
    return render(request, "movimentecao/home.html", {})


class FinListView(ListView):
    model = db_financeiro
    template_name = "movimentecao/fin_list.html"
    context_object_name = "fin_list"


class Total(ListView):
    model = db_financeiro
    template_name = "movimentecao/total.html"
    context_object_name = "total"

    def get_queryset(self):
        context = db_financeiro.objects.filter(tbl_tipo="E").aggregate(Sum("tbl_valor"))
        context["fin_list"] = db_financeiro.objects.all()
        total_saida = db_financeiro.objects.filter(tbl_tipo="S").aggregate(
            Sum("tbl_valor")
        )
        total_entrada = db_financeiro.objects.filter(tbl_tipo="E").aggregate(
            Sum("tbl_valor")
        )
        if total_entrada.get("tbl_valor__sum") is None:
            total_entrada["tbl_valor__sum"] = 0
        if total_saida.get("tbl_valor__sum") is None:
            total_saida["tbl_valor__sum"] = 0
        total = total_entrada.get("tbl_valor__sum") - total_saida.get("tbl_valor__sum")
        context["fin_total"] = total
        return context


class FinUpdateView(UpdateView):
    model = db_financeiro
    fields = "__all__"
    template_name = "movimentecao/fin_form.html"
    success_url = reverse_lazy("fin_list")


class FinDeleteView(DeleteView):
    model = db_financeiro
    template_name = "movimentecao/fin_delete.html"
    success_url = reverse_lazy("fin_list")


def movcad(request):
    if request.method == "POST":
        form = MovimentecaoForm(request.POST)
        mov = db_financeiro()
        mov.tbl_data = request.POST.get("data")
        mov.tbl_movimentacao = request.POST.get("descricao")
        mov.tbl_valor = request.POST.get("valor")
        mov.tbl_tipo = request.POST.get("tipo")
        mov.save()
        return redirect("fin_list")
    else:
        form = MovimentecaoForm()
        context = {"form": form}
        context["mensagem"] = "Movimentação Cadastrada"
        form = MovimentecaoForm()
        return render(request, "movimentecao/finmov.html", context)
