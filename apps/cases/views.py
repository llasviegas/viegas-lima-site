from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import CaseEstudo


def index(request):
    qs = CaseEstudo.objects.filter(publicado=True)
    paginator = Paginator(qs, 6)
    page = paginator.get_page(request.GET.get("page"))
    return render(request, "cases/index.html", {
        "page_obj": page,
        "meta_title": "Cases de Sucesso | Viegas & Lima",
        "meta_description": "Veja como ajudamos empresas a economizar tributos, vencer autuações e estruturar operações.",
    })


def detalhe(request, slug):
    case = get_object_or_404(CaseEstudo, slug=slug, publicado=True)
    relacionados = CaseEstudo.objects.filter(publicado=True).exclude(pk=case.pk)[:3]
    return render(request, "cases/detalhe.html", {
        "case": case,
        "relacionados": relacionados,
        "meta_title": case.meta_title or case.titulo[:70],
        "meta_description": case.meta_description or case.resumo[:160],
    })
