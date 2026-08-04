from django.contrib.sitemaps import Sitemap
from .models import Artigo


class BlogSitemap(Sitemap):
    priority = 0.7
    changefreq = "weekly"

    def items(self):
        return Artigo.objects.filter(publicado=True)

    def lastmod(self, obj):
        return obj.data_atualizacao

    def location(self, obj):
        return obj.get_absolute_url()
