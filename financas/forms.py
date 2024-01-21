# financas/forms.py
from django import forms
from .models import Despesa, Receita


class DespesaForm(forms.ModelForm):
    class Meta:
        model = Despesa
        fields = ["descricao", "valor", "data"]
        widgets = {
            # "data": forms.DateInput(attrs={"type": "date"}),
            "data": forms.TextInput(attrs={"type": "date"}),
        }


class ReceitaForm(forms.ModelForm):
    class Meta:
        model = Receita
        fields = ["descricao", "valor", "data"]
        widgets = {
            # "data": forms.DateInput(attrs={"type": "date"}),
            "data": forms.TextInput(attrs={"type": "date"}),
        }
