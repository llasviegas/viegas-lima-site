from django.contrib import admin
from .models import Lead


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ("nome", "email", "empresa", "area", "created_at", "lido")
    list_filter = ("area", "lido", "created_at")
    search_fields = ("nome", "email", "empresa", "mensagem")
    readonly_fields = ("created_at", "ip_origem")
