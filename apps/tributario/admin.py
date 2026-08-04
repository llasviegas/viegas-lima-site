from django.contrib import admin
from .models import PaginaTributario


@admin.register(PaginaTributario)
class PaginaTributarioAdmin(admin.ModelAdmin):
    list_display = ("titulo", "destaque_home", "ativo", "ordem")
    list_filter = ("ativo", "destaque_home")
    search_fields = ("titulo", "descricao_curta", "conteudo")
    prepopulated_fields = {"slug": ("titulo",)}
