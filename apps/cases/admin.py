from django.contrib import admin
from .models import CaseEstudo


@admin.register(CaseEstudo)
class CaseEstudoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "cliente_ficticio", "setor", "publicado", "destaque", "data_publicacao")
    list_filter = ("publicado", "destaque", "setor")
    search_fields = ("titulo", "cliente_ficticio", "resumo", "problema")
    prepopulated_fields = {"slug": ("titulo",)}
