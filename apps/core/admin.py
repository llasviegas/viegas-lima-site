from django.contrib import admin
from .models import ConfiguracaoSite, Depoimento, Numerico


@admin.register(ConfiguracaoSite)
class ConfiguracaoSiteAdmin(admin.ModelAdmin):
    list_display = ("site", "telefone", "email", "oab")


@admin.register(Depoimento)
class DepoimentoAdmin(admin.ModelAdmin):
    list_display = ("nome", "cargo_empresa", "estrelas", "ativo", "ordem")
    list_filter = ("ativo", "estrelas")
    search_fields = ("nome", "cargo_empresa", "texto")


@admin.register(Numerico)
class NumericoAdmin(admin.ModelAdmin):
    list_display = ("valor", "rotulo", "ordem", "ativo")
    list_filter = ("ativo",)
