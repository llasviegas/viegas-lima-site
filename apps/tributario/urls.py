from django.urls import path
from . import views

app_name = "tributario"

urlpatterns = [
    path("", views.index, name="index"),
    path("planejamento/", views.planejamento, name="planejamento"),
    path("contencioso/", views.contencioso, name="contencioso"),
    path("recuperacao/", views.recuperacao, name="recuperacao"),
    path("reforma/", views.reforma, name="reforma"),
    path("ma/", views.ma, name="ma"),
]
