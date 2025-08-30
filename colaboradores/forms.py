from django import forms
from .models import Colaborador

class ColaboradorForm(forms.ModelForm):
    class Meta:
        model = Colaborador
        fields = ["nome", "cpf", "matricula", "ativo"]
        widgets = {
            "nome": forms.TextInput(attrs={"class":"in"}),
            "cpf": forms.TextInput(attrs={"class":"in","maxlength":"11"}),
            "matricula": forms.TextInput(attrs={"class":"in"}),
            "ativo": forms.CheckboxInput(attrs={"class":"ck"}),
        }
