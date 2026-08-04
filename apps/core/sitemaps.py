from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = "monthly"

    def items(self):
        return [
            "core:home",
            "core:sobre",
            "core:equipe",
            "tributario:index",
            "tributario:planejamento",
            "tributario:contencioso",
            "tributario:recuperacao",
            "tributario:reforma",
            "tributario:ma",
            "empresarial:index",
            "civil:index",
            "trabalhista:index",
            "previdenciario:index",
            "familia:index",
            "cases:index",
            "blog:index",
            "leads:contato",
        ]

    def location(self, item):
        return reverse(item)
