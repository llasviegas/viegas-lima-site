from django.contrib import admin
from .models import PaginaEmpresarial


@admin.register(PaginaEmpresarial)
class PaginaEmpresarialAdmin(admin.ModelAdmin):
    list_display = ("titulo", "ativo", "ordem")
    list_filter = ("ativo",)
    search_fields = ("titulo",)
    prepopulated_fields = {"slug": ("titulo",)}
