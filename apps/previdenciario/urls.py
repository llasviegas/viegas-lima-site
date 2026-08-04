from django.urls import path
from . import views

app_name = "previdenciario"

urlpatterns = [
    path("", views.index, name="index"),
]
