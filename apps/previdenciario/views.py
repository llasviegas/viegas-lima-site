from django.shortcuts import render


def index(request):
    return render(request, "previdenciario/index.html", {
        "meta_title": "Direito Previdenciário | Viegas & Lima",
        "meta_description": "Aposentadoria, revisões, benefícios por incapacidade e planejamento previdenciário.",
    })
