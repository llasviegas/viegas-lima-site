from django.shortcuts import render, get_object_or_404
from django.contrib.sites.models import Site

from .models import ConfiguracaoSite, Depoimento, Numerico
from apps.cases.models import CaseEstudo
from apps.blog.models import Artigo
from apps.tributario.models import PaginaTributario


def _get_config():
    site = Site.objects.get_current()
    config, _ = ConfiguracaoSite.objects.get_or_create(site=site)
    return config


def home(request):
    config = _get_config()
    indicadores = Numerico.objects.filter(ativo=True)
    depoimentos = Depoimento.objects.filter(ativo=True)[:6]
    cases = CaseEstudo.objects.filter(publicado=True, destaque=True)[:3]
    artigos = Artigo.objects.filter(publicado=True)[:3]
    tributario_pages = PaginaTributario.objects.filter(ativo=True)

    return render(request, "core/home.html", {
        "config": config,
        "indicadores": indicadores,
        "depoimentos": depoimentos,
        "cases": cases,
        "artigos": artigos,
        "tributario_pages": tributario_pages,
    })


def sobre(request):
    config = _get_config()
    return render(request, "core/sobre.html", {"config": config})


def equipe(request):
    config = _get_config()
    return render(request, "core/equipe.html", {"config": config})


def custom_404(request, exception=None):
    config = _get_config()
    return render(request, "core/404.html", {"config": config}, status=404)


def custom_500(request):
    config = _get_config()
    return render(request, "core/500.html", {"config": config}, status=500)
