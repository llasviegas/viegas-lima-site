from django.shortcuts import render


def index(request):
    return render(request, "familia/index.html", {
        "meta_title": "Direito de Família | Viegas & Lima",
        "meta_description": "Divórcio, inventário, guarda, partilha de bens e planejamento patrimonial familiar.",
    })
