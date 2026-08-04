from django.shortcuts import render


def index(request):
    return render(request, "empresarial/index.html", {
        "meta_title": "Direito Empresarial e M&A | Viegas & Lima",
        "meta_description": "Assessoria jurídica em fusões, aquisições, contratos empresariais e reestruturações societárias.",
    })
