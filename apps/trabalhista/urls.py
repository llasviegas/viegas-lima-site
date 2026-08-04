from django.urls import path
from . import views

app_name = "trabalhista"

urlpatterns = [
    path("", views.index, name="index"),
]
