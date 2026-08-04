from django.contrib import admin
from .models import PaginaTrabalhista


@admin.register(PaginaTrabalhista)
class PaginaTrabalhistaAdmin(admin.ModelAdmin):
    list_display = ("titulo", "ativo", "ordem")
    list_filter = ("ativo",)
    prepopulated_fields = {"slug": ("titulo",)}
