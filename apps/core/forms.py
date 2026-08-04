from django import forms
from .models import ConfiguracaoSite


class ConfiguracaoSiteForm(forms.ModelForm):
    class Meta:
        model = ConfiguracaoSite
        fields = "__all__"


class DepoimentoForm(forms.ModelForm):
    class Meta:
        model = Depoimento
        fields = "__all__"


class NumericoForm(forms.ModelForm):
    class Meta:
        model = Numerico
        fields = "__all__"
