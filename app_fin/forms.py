from django import forms


class MovimentecaoForm(forms.Form):
    descricao = forms.CharField(max_length=100)
    data = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    tipo = forms.ChoiceField(choices=(("E", "Entrada"), ("S", "Saida")))
    valor = forms.DecimalField(max_digits=10, decimal_places=2)
