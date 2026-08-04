from django.shortcuts import render
from .models import PaginaTributario


def _get_or_default(slug, titulo_default, descricao_default):
    try:
        return PaginaTributario.objects.get(slug=slug, ativo=True)
    except PaginaTributario.DoesNotExist:
        return None


def index(request):
    paginas = PaginaTributario.objects.filter(ativo=True).order_by("ordem")
    return render(request, "tributario/index.html", {
        "paginas": paginas,
        "meta_title": "Direito Tributário Estratégico | Viegas & Lima",
        "meta_description": "Planejamento tributário, contencioso fiscal, recuperação de créditos e M&A com viés tributário para grandes negócios.",
    })


def planejamento(request):
    return render(request, "tributario/planejamento.html", {
        "meta_title": "Planejamento Tributário | Viegas & Lima",
        "meta_description": "Reduza a carga tributária da sua empresa com planejamento tributário legal e estratégico. Atendimento personalizado para médias e grandes empresas.",
    })


def contencioso(request):
    return render(request, "tributario/contencioso.html", {
        "meta_title": "Contencioso Fiscal Estratégico | Viegas & Lima",
        "meta_description": "Defesa especializada em autos de infração, execuções fiscais e processos administrativos tributários.",
    })


def recuperacao(request):
    return render(request, "tributario/recuperacao.html", {
        "meta_title": "Recuperação de Créditos Tributários | Viegas & Lima",
        "meta_description": "Recupere PIS, COFINS, ICMS, IRPJ e outros tributos pagos a mais nos últimos 5 anos.",
    })


def reforma(request):
    return render(request, "tributario/reforma.html", {
        "meta_title": "Reforma Tributária IBS/CBS 2026 | Viegas & Lima",
        "meta_description": "Prepare sua empresa para a Reforma Tributária. Análise de impactos e oportunidades do IBS e CBS.",
    })


def ma(request):
    return render(request, "tributario/ma.html", {
        "meta_title": "M&A com Due Diligence Tributária | Viegas & Lima",
        "meta_description": "Assessoria tributária em fusões, aquisições e reestruturações societárias.",
    })
