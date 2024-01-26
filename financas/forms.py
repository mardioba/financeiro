# financas/forms.py
from django import forms
from .models import Despesa, Receita
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, UserCreationForm

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

class LoginForm(AuthenticationForm):
    # Adicione campos personalizados, se necessário
    pass


class ChangePasswordForm(PasswordChangeForm):
    # Adicione campos personalizados, se necessário
    pass

class SignupForm(UserCreationForm):
    # Adicione campos personalizados, se necessário
    pass