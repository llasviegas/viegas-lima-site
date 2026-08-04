from django.contrib import admin
from .models import PaginaPrevidenciario


@admin.register(PaginaPrevidenciario)
class PaginaPrevidenciarioAdmin(admin.ModelAdmin):
    list_display = ("titulo", "ativo", "ordem")
    list_filter = ("ativo",)
    prepopulated_fields = {"slug": ("titulo",)}
