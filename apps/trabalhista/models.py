from django.db import models


class PaginaTrabalhista(models.Model):
    slug = models.SlugField(unique=True)
    titulo = models.CharField(max_length=180)
    descricao_curta = models.CharField(max_length=255)
    conteudo = models.TextField()
    ordem = models.IntegerField(default=0)
    ativo = models.BooleanField(default=True)
    meta_title = models.CharField(max_length=70, blank=True)
    meta_description = models.CharField(max_length=160, blank=True)

    class Meta:
        ordering = ["ordem", "titulo"]
        verbose_name = "Página Trabalhista"
        verbose_name_plural = "Páginas Trabalhistas"

    def __str__(self):
        return self.titulo
