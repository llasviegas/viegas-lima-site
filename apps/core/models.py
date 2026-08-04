from django.db import models
from django.contrib.sites.models import Site


class ConfiguracaoSite(models.Model):
    """Configurações globais do site (telefone, e-mail, endereço, redes sociais)."""
    site = models.OneToOneField(Site, on_delete=models.CASCADE, related_name="configuracao")
    telefone = models.CharField(max_length=20, blank=True, default="(61) 99999-9999")
    whatsapp = models.CharField(max_length=20, blank=True, default="5561999999999")
    email = models.EmailField(default="contato@viegaselima.com.br")
    endereco = models.CharField(max_length=255, blank=True, default="Ceilândia-DF")
    cnpj = models.CharField(max_length=20, blank=True)
    oab = models.CharField(max_length=50, default="OAB/DF 36.362")
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    youtube = models.URLField(blank=True)
    whatsapp_mensagem = models.CharField(
        max_length=255,
        default="Olá, gostaria de uma consulta sobre direito tributário.",
    )

    class Meta:
        verbose_name = "Configuração do Site"
        verbose_name_plural = "Configurações do Site"

    def __str__(self):
        return f"Configuração {self.site.domain}"


class Depoimento(models.Model):
    """Depoimentos (ilustrativos, sem dados reais de clientes)."""
    nome = models.CharField(max_length=120)
    cargo_empresa = models.CharField(max_length=180, blank=True)
    texto = models.TextField()
    estrelas = models.IntegerField(default=5, choices=[(i, i) for i in range(1, 6)])
    ativo = models.BooleanField(default=True)
    ordem = models.IntegerField(default=0)

    class Meta:
        ordering = ["ordem", "nome"]
        verbose_name = "Depoimento"
        verbose_name_plural = "Depoimentos"

    def __str__(self):
        return f"{self.nome} — {self.cargo_empresa}"


class Numerico(models.Model):
    """Indicadores numéricos da home (ex: 150+ casos, 15 anos, R$ economizados)."""
    valor = models.CharField(max_length=20, help_text="Ex: '150+', 'R$ 50M', '15'")
    rotulo = models.CharField(max_length=120, help_text="Ex: 'Casos resolvidos'")
    descricao = models.CharField(max_length=255, blank=True)
    icone = models.CharField(max_length=4, default="⚖️", help_text="Emoji opcional")
    ordem = models.IntegerField(default=0)
    ativo = models.BooleanField(default=True)

    class Meta:
        ordering = ["ordem", "valor"]
        verbose_name = "Indicador Numérico"
        verbose_name_plural = "Indicadores Numéricos"

    def __str__(self):
        return f"{self.valor} {self.rotulo}"
