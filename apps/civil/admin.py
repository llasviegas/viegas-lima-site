from django.contrib import admin
from .models import PaginaCivil


@admin.register(PaginaCivil)
class PaginaCivilAdmin(admin.ModelAdmin):
    list_display = ("titulo", "ativo", "ordem")
    list_filter = ("ativo",)
    prepopulated_fields = {"slug": ("titulo",)}
