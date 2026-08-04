from django.db import models


class PaginaTributario(models.Model):
    """Sub-páginas da área Tributário (carro-chefe do site)."""
    slug = models.SlugField(unique=True, max_length=80)
    titulo = models.CharField(max_length=180)
    subtitulo = models.CharField(max_length=255, blank=True)
    descricao_curta = models.CharField(max_length=255, help_text="Usada em cards e meta description")
    conteudo = models.TextField(help_text="HTML ou Markdown")
    icone = models.CharField(max_length=4, default="⚖️")
    cor_destaque = models.CharField(max_length=20, default="#B8860B")
    ordem = models.IntegerField(default=0)
    ativo = models.BooleanField(default=True)
    destaque_home = models.BooleanField(default=False, help_text="Mostrar na home?")
    meta_title = models.CharField(max_length=70, blank=True)
    meta_description = models.CharField(max_length=160, blank=True)

    class Meta:
        ordering = ["ordem", "titulo"]
        verbose_name = "Página Tributário"
        verbose_name_plural = "Páginas Tributário"

    def __str__(self):
        return self.titulo
