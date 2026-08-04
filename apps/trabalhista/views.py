from django.shortcuts import render


def index(request):
    return render(request, "trabalhista/index.html", {
        "meta_title": "Direito Trabalhista Empresarial | Viegas & Lima",
        "meta_description": "Assessoria preventiva e contenciosa em relações de trabalho. Foco em empregadores.",
    })
