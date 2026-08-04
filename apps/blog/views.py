from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Artigo, Categoria


def index(request):
    qs = Artigo.objects.filter(publicado=True).select_related("categoria")
    categoria_slug = request.GET.get("categoria")
    if categoria_slug:
        qs = qs.filter(categoria__slug=categoria_slug)
    paginator = Paginator(qs, 9)
    page = paginator.get_page(request.GET.get("page"))
    categorias = Categoria.objects.all()
    return render(request, "blog/index.html", {
        "page_obj": page,
        "categorias": categorias,
        "meta_title": "Blog Jurídico | Viegas & Lima",
        "meta_description": "Artigos sobre direito tributário, empresarial e Reforma Tributária.",
    })


def categoria(request, slug):
    categoria = get_object_or_404(Categoria, slug=slug)
    return redirect(f"/blog/?categoria={slug}")  # Simplificado


def detalhe(request, slug):
    artigo = get_object_or_404(Artigo, slug=slug, publicado=True)
    # incrementa visualizações
    Artigo.objects.filter(pk=artigo.pk).update(visualizacoes=artigo.visualizacoes + 1)
    relacionados = Artigo.objects.filter(publicado=True).exclude(pk=artigo.pk)[:3]
    return render(request, "blog/detalhe.html", {
        "artigo": artigo,
        "relacionados": relacionados,
        "meta_title": artigo.meta_title or artigo.titulo[:70],
        "meta_description": artigo.meta_description or artigo.resumo[:160],
    })
