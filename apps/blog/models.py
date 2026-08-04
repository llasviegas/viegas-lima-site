from django.db import models
from django.utils.text import slugify


class Categoria(models.Model):
    nome = models.CharField(max_length=80)
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        ordering = ["nome"]
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome


class Artigo(models.Model):
    titulo = models.CharField(max_length=180)
    slug = models.SlugField(unique=True, max_length=200, blank=True)
    resumo = models.TextField(help_text="Resumo para cards e meta description", blank=True)
    corpo = models.TextField(help_text="Conteúdo em Markdown ou HTML")
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True, related_name="artigos")
    imagem_destaque = models.ImageField(upload_to="blog/", blank=True)
    autor = models.CharField(max_length=120, default="Lucas Viegas")
    publicado = models.BooleanField(default=False)
    destaque = models.BooleanField(default=False, help_text="Aparece na home?")
    data_publicacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    visualizacoes = models.PositiveIntegerField(default=0)
    tempo_leitura_min = models.PositiveIntegerField(default=5)
    meta_title = models.CharField(max_length=70, blank=True)
    meta_description = models.CharField(max_length=160, blank=True)
    tags = models.CharField(max_length=255, blank=True, help_text="Tags separadas por vírgula")

    class Meta:
        ordering = ["-data_publicacao"]
        verbose_name = "Artigo"
        verbose_name_plural = "Artigos"

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.titulo)[:200]
            slug = base_slug
            n = 1
            while Artigo.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{n}"
                n += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("blog:detalhe", kwargs={"slug": self.slug})

    @property
    def tag_list(self):
        return [t.strip() for t in self.tags.split(",") if t.strip()]
