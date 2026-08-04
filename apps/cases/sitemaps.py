from django.contrib.sitemaps import Sitemap
from .models import CaseEstudo


class CaseSitemap(Sitemap):
    priority = 0.6
    changefreq = "monthly"

    def items(self):
        return CaseEstudo.objects.filter(publicado=True)

    def lastmod(self, obj):
        return obj.data_publicacao

    def location(self, obj):
        return obj.get_absolute_url()
