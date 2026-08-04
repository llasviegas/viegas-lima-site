from django.contrib import admin
from .models import PaginaFamilia


@admin.register(PaginaFamilia)
class PaginaFamiliaAdmin(admin.ModelAdmin):
    list_display = ("titulo", "ativo", "ordem")
    list_filter = ("ativo",)
    prepopulated_fields = {"slug": ("titulo",)}
