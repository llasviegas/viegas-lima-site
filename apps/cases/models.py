from django.db import models
from django.utils.text import slugify


class Setor(models.TextChoices):
    INDUSTRIA = "industria", "Indústria"
    SERVICOS = "servicos", "Serviços"
    COMERCIO = "comercio", "Comércio"
    TECNOLOGIA = "tecnologia", "Tecnologia"
    SAUDE = "saude", "Saúde"
    EDUCACAO = "educacao", "Educação"
    AGRO = "agro", "Agronegócio"
    CONSTRUCAO = "construcao", "Construção"
    OUTRO = "outro", "Outro"


class CaseEstudo(models.Model):
    titulo = models.CharField(max_length=180)
    slug = models.SlugField(unique=True, max_length=200, blank=True)
    cliente_ficticio = models.CharField(max_length=120, help_text="Nome fictício pra ilustrar")
    setor = models.CharField(max_length=20, choices=Setor.choices, default=Setor.OUTRO)
    resumo = models.TextField(help_text="Resumo do desafio + resultado em 1 parágrafo")
    problema = models.TextField(help_text="Qual era o problema/dor do cliente")
    solucao = models.TextField(help_text="O que fizemos")
    resultado = models.TextField(help_text="Resultado obtido (incluir números se possível)")
    resultado_numero = models.CharField(max_length=50, blank=True, help_text="Ex: 'R$ 2,5M economizados'")
    duracao = models.CharField(max_length=80, blank=True, help_text="Ex: '8 meses'")
    publicado = models.BooleanField(default=False)
    destaque = models.BooleanField(default=False, help_text="Aparece na home?")
    data_publicacao = models.DateTimeField(auto_now_add=True)
    meta_title = models.CharField(max_length=70, blank=True)
    meta_description = models.CharField(max_length=160, blank=True)

    class Meta:
        ordering = ["-data_publicacao"]
        verbose_name = "Case de Estudo"
        verbose_name_plural = "Cases de Estudo"

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.titulo)[:200]
            slug = base_slug
            n = 1
            while CaseEstudo.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{n}"
                n += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.cliente_ficticio} — {self.titulo}"

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("cases:detalhe", kwargs={"slug": self.slug})
