from django import forms
from .models import Lead


class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ("nome", "email", "telefone", "empresa", "cargo", "area", "mensagem")
        widgets = {
            "nome": forms.TextInput(attrs={"class": "vl-input", "placeholder": "Seu nome completo"}),
            "email": forms.EmailInput(attrs={"class": "vl-input", "placeholder": "seu@email.com"}),
            "telefone": forms.TextInput(attrs={"class": "vl-input", "placeholder": "(61) 99999-9999"}),
            "empresa": forms.TextInput(attrs={"class": "vl-input", "placeholder": "Sua empresa"}),
            "cargo": forms.TextInput(attrs={"class": "vl-input", "placeholder": "Seu cargo"}),
            "area": forms.Select(attrs={"class": "vl-input"}),
            "mensagem": forms.Textarea(attrs={"class": "vl-input", "rows": 5, "placeholder": "Conte um pouco sobre o seu caso..."}),
        }

    def clean_nome(self):
        nome = self.cleaned_data["nome"].strip()
        if len(nome) < 3:
            raise forms.ValidationError("Nome muito curto.")
        return nome

    def clean_mensagem(self):
        msg = self.cleaned_data["mensagem"].strip()
        if len(msg) < 10:
            raise forms.ValidationError("Por favor, detalhe um pouco mais.")
        return msg
