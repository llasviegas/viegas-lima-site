from django.contrib import admin
from .models import Artigo, Categoria


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nome", "slug")
    prepopulated_fields = {"slug": ("nome",)}


@admin.register(Artigo)
class ArtigoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "categoria", "publicado", "destaque", "data_publicacao", "visualizacoes")
    list_filter = ("publicado", "destaque", "categoria")
    search_fields = ("titulo", "resumo", "corpo")
    prepopulated_fields = {"slug": ("titulo",)}
    readonly_fields = ("visualizacoes", "data_publicacao", "data_atualizacao")
