from django.urls import path
from . import views

app_name = "familia"

urlpatterns = [
    path("", views.index, name="index"),
]
