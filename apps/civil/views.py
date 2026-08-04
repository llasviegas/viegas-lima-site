from django.shortcuts import render


def index(request):
    return render(request, "civil/index.html", {
        "meta_title": "Direito Cível | Viegas & Lima",
        "meta_description": "Assessoria em contratos, responsabilidade civil, direito do consumidor e obrigações.",
    })
