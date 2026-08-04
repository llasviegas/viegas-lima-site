from django.urls import path
from . import views

app_name = "leads"

urlpatterns = [
    path("", views.contato, name="contato"),
    path("obrigado/", views.obrigado, name="obrigado"),
]
