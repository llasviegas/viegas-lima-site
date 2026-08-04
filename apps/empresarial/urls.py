from django.urls import path
from . import views

app_name = "empresarial"

urlpatterns = [
    path("", views.index, name="index"),
]
