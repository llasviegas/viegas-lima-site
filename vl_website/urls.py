"""
URL Configuration for vl_website.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView

from apps.core.sitemaps import StaticViewSitemap
from apps.blog.sitemaps import BlogSitemap
from apps.cases.sitemaps import CaseSitemap

sitemaps = {
    "static": StaticViewSitemap,
    "blog": BlogSitemap,
    "cases": CaseSitemap,
}

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.core.urls")),
    path("tributario/", include("apps.tributario.urls")),
    path("empresarial/", include("apps.empresarial.urls")),
    path("civil/", include("apps.civil.urls")),
    path("trabalhista/", include("apps.trabalhista.urls")),
    path("previdenciario/", include("apps.previdenciario.urls")),
    path("familia/", include("apps.familia.urls")),
    path("blog/", include("apps.blog.urls")),
    path("cases/", include("apps.cases.urls")),
    path("contato/", include("apps.leads.urls")),

    # SEO
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    path(
        "robots.txt",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Custom 404/500
handler404 = "apps.core.views.custom_404"
handler500 = "apps.core.views.custom_500"
