from django.db import models


class AreaInteresse(models.TextChoices):
    TRIBUTARIO = "tributario", "Direito Tributário"
    EMPRESARIAL = "empresarial", "Direito Empresarial / M&A"
    CIVIL = "civil", "Direito Cível"
    TRABALHISTA = "trabalhista", "Direito Trabalhista"
    PREVIDENCIARIO = "previdenciario", "Direito Previdenciário"
    FAMILIA = "familia", "Direito de Família"
    OUTRO = "outro", "Outro"


class Lead(models.Model):
    nome = models.CharField(max_length=120)
    email = models.EmailField()
    telefone = models.CharField(max_length=20, blank=True)
    empresa = models.CharField(max_length=180, blank=True)
    cargo = models.CharField(max_length=120, blank=True)
    area = models.CharField(max_length=30, choices=AreaInteresse.choices, default=AreaInteresse.TRIBUTARIO)
    mensagem = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    lido = models.BooleanField(default=False)
    ip_origem = models.GenericIPAddressField(null=True, blank=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Lead"
        verbose_name_plural = "Leads"

    def __str__(self):
        return f"{self.nome} <{self.email}> — {self.area}"
