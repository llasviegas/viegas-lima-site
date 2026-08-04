"""
Seed inicial do banco — popula dados de exemplo (fictícios) pra o site não ficar vazio.
Execute com: python manage.py shell < seed.py
"""

import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vl_website.settings")
django.setup()

from django.contrib.sites.models import Site
from apps.core.models import ConfiguracaoSite, Numerico, Depoimento
from apps.tributario.models import PaginaTributario
from apps.blog.models import Categoria, Artigo
from apps.cases.models import CaseEstudo
from django.utils.text import slugify

print("→ Configurando site...")
site, _ = Site.objects.update_or_create(
    id=1,
    defaults={"domain": "viegaselima.com.br", "name": "Viegas & Lima Advocacia"},
)

print("→ Criando configuração...")
config, _ = ConfiguracaoSite.objects.update_or_create(
    site=site,
    defaults={
        "telefone": "(61) 99999-9999",
        "whatsapp": "5561999999999",
        "email": "contato@viegaselima.com.br",
        "endereco": "Ceilândia-DF",
        "oab": "OAB/DF 36.362",
        "linkedin": "https://linkedin.com/company/viegas-e-lima",
        "instagram": "https://instagram.com/viegaselima",
        "whatsapp_mensagem": "Olá, gostaria de uma consulta sobre direito tributário.",
    },
)

print("→ Criando indicadores numéricos...")
indicadores = [
    ("150+", "Casos Atendidos", "Empresas assessoradas", "⚖️", 1),
    ("R$ 30M+", "Economizados", "Em tributos recuperados", "💰", 2),
    ("15", "Anos de Experiência", "Advocacia tributária e empresarial", "�", 3),
    ("98%", "Clientes Satisfeitos", "Taxa de recomendação", "⭐", 4),
]
for valor, rotulo, desc, icone, ordem in indicadores:
    Numerico.objects.update_or_create(
        rotulo=rotulo,
        defaults={
            "valor": valor, "descricao": desc, "icone": icone, "ordem": ordem, "ativo": True,
        },
    )

print("→ Criando depoimentos fictícios...")
depoimentos = [
    ("Carlos Mendes", "Diretor Financeiro, Empresa Industrial A", "A equipe da Viegas & Lima identificou créditos de PIS/COFINS que não sabíamos que tínhamos direito. Recuperamos R$ 1,2M em 6 meses.", 5, 1),
    ("Patricia Souza", "CEO, Grupo Varejo B", "O planejamento tributário reduziu nossa carga em 22% sem mudar a operação. Atendimento técnico e próximo.", 5, 2),
    ("Roberto Almeida", "Sócio, Holding Patrimonial C", "Profissionais de confiança. Resolveram um auto de infração complexo sem custos adicionais além do contratado.", 5, 3),
    ("Juliana Costa", "Diretora Jurídica, Empresa de Serviços D", "Excelente trabalho na due diligence tributária da nossa aquisição. Evitamos um passivo de R$ 3M.", 5, 4),
]
for nome, cargo, texto, estrelas, ordem in depoimentos:
    Depoimento.objects.update_or_create(
        nome=nome,
        defaults={"cargo_empresa": cargo, "texto": texto, "estrelas": estrelas, "ordem": ordem, "ativo": True},
    )

print("→ Criando categorias do blog...")
cats = {
    "Direito Tributário": "Artigos sobre planejamento, contencioso e recuperação de créditos tributários.",
    "Reforma Tributária": "Análises sobre IBS, CBS e o impacto da Reforma 2026-2033 nas empresas.",
    "Direito Empresarial": "M&A, contratos, governança e reestruturações societárias.",
    "Contencioso Fiscal": "Defesas em autos de infração, teses tributárias e jurisprudência.",
}
for nome, desc in cats.items():
    cat, _ = Categoria.objects.get_or_create(nome=nome, defaults={"slug": slugify(nome)})

print("→ Criando artigos do blog...")
artigos_data = [
    {
        "titulo": "Reforma Tributária 2026: o que muda para empresas do Lucro Real",
        "resumo": "Análise do impacto da Reforma Tributária (EC 132/2023) nas empresas optantes do Lucro Real. Mudanças no PIS, COFINS, ICMS e ISS com a chegada do IBS e CBS.",
        "corpo": """A Reforma Tributária do consumo (EC 132/2023) é a maior mudança estrutural do sistema tributário brasileiro desde 1988. Para empresas do Lucro Real, o impacto é direto: a carga tributária total será afetada pela substituição de PIS, COFINS, IPI, ICMS e ISS por IBS (estadual/municipal) e CBS (federal).

## O que muda na prática

A partir de 2026, inicia-se a transição gradual que se estenderá até 2033. As alíquotas de IBS e CBS serão definidas pelo Comitê Gestor do IBS, mas estimativas indicam:

- **Carga total hoje**: ~32% sobre o faturamento
- **Carga estimada pós-Reforma**: 25% a 28%

Para empresas do Lucro Real com alta margem, isso pode representar economia real. Mas atenção: a carga setorial varia enormemente. Serviços tendem a ser mais tributados; indústria pode ser beneficiada.

## Cronograma resumido

- **2026**: Início da cobrança da CBS (federal)
- **2027-2028**: Período de testes do IBS
- **2029-2032**: Transição gradual
- **2033**: Extinção completa de PIS/COFINS/ICMS/ISS

## O que sua empresa precisa fazer AGORA

1. Mapear a cadeia produtiva atual e identificar créditos de PIS/COFINS disponíveis
2. Avaliar se o regime atual (Lucro Real) permanece vantajoso
3. Planejar a reorganização societária para otimização fiscal
4. Preparar sistemas ERP e fiscal para a mudança
5. Consultar advogado especializado — cada caso é único

Quer saber o impacto específico na sua empresa? Agende uma análise estratégica.""",
        "categoria_nome": "Reforma Tributária",
        "autor": "Lucas Viegas",
        "tempo_leitura_min": 8,
        "tags": "reforma tributária, IBS, CBS, Lucro Real",
        "publicado": True,
        "destaque": True,
    },
    {
        "titulo": "Transação Tributária: como sua empresa pode pagar menos com segurança jurídica",
        "resumo": "A Transação Tributária (Lei 14.689/2023) permite negociar descontos de até 50% em dívidas com a União. Veja quando faz sentido para sua empresa.",
        "corpo": """A Transação Tributária é uma das ferramentas mais eficazes para empresas com débitos junto à Receita Federal ou Procuradoria-Geral da Fazenda Nacional (PGFN). Regulamentada pela Lei 14.689/2023 e pelo Portaria PGFN/ME nº 6.757/2022, permite negociação com descontos e prazos vantajosos.

## Modalidades disponíveis

A PGFN oferece atualmente:

- **Transação por Adesão (Extrajudicial)**: descontos de até 50% sobre o valor principal
- **Transação Individual**: negociada caso a caso para débitos acima de R$ 10M
- **Transação no Contencioso**: aplicação de até 50% de desconto + parcelamento

## Vantagens concretas

- Descontos sobre juros e multas (até 100% sobre multas qualificadas)
- Parcelamento em até 145 meses
- Possibilidade de usar prejuízo fiscal e base negativa de CSLL para amortizar débitos
- Suspensão de protestos e execuções fiscais durante a negociação

## Quando vale a pena?

A transação é especialmente vantajosa para:

- Empresas em dificuldade financeira com débitos antigos
- Débitos com discussão judicial em andamento (transação no contencioso)
- Situações em que o desconto compensa o custo do processo

## Cuidados importantes

A transação exige confissão de dívida. Por isso, antes de aderir:

1. Analise se realmente há o débito (alguns são discutíveis)
2. Avalie o impacto contábil (passivo continua existindo até quitação)
3. Compare com cenários de vitória judicial (especialmente débitos do SIMPLES)

Quer avaliar se sua empresa tem débitos negociáveis? Faça uma consulta estratégica.""",
        "categoria_nome": "Direito Tributário",
        "autor": "Lucas Viegas",
        "tempo_leitura_min": 7,
        "tags": "transação tributária, PGFN, dívida ativa, parcelamento",
        "publicado": True,
        "destaque": True,
    },
    {
        "titulo": "5 sinais de que sua empresa está pagando tributo a mais",
        "resumo": "Indicadores práticos que mostram oportunidades de recuperação tributária. Se algum desses se aplica à sua empresa, há dinheiro na mesa.",
        "corpo": """Nem sempre é fácil saber se sua empresa está pagando mais tributo do que deveria. Tributação é complexa e muitas oportunidades passam despercebidas. Aqui estão 5 sinais clássicos de que há espaço para economia:

## 1. Você paga ICMS-ST em quase todas as compras

Se sua empresa é contribuinte do ICMS e compra mercadorias com substituição tributária, há grande chance de ter créditos a recuperar. A análise depende do seu CNAE e tipo de mercadoria.

## 2. Nunca revisou os créditos de PIS/COFINS sobre insumos

A Receita Federal tem interpretação restritiva, mas o STJ (Tema 779) reconheceu o direito a créditos sobre insumos essenciais. Se você nunca analisou, pode ter 5 anos de créditos não aproveitados.

## 3. Sua empresa paga PIS/COFINS sobre ICMS

O STF (Tema 69) decidiu em 2021 que o ICMS não compõe a base de PIS/COFINS. Se sua empresa ainda não recuperou esses valores pagos desde 2017, há oportunidade real — embora o prazo decadencial esteja se aproximando.

## 4. Regime tributário escolhido por inércia

Muitos empresários permanecem no Lucro Real por opção do contador há 10 anos, sem reavaliação. Dependendo do setor e margem, o Lucro Presumido pode ser mais vantajoso — e a mudança é permitida 1x por ano.

## 5. Auto de infração "engavetado" sem análise

Se há auto de infração antigo que "ninguém mexeu", há chances reais de nulidade por vício formal (decadência, ilegitimidade, falta de motivação). Não pague sem antes analisar.

## Próximo passo

Se sua empresa tem 1 ou mais desses sinais, vale uma análise tributária profissional. Identificamos onde está o dinheiro e o que pode ser recuperado legalmente.""",
        "categoria_nome": "Direito Tributário",
        "autor": "Lucas Viegas",
        "tempo_leitura_min": 6,
        "tags": "recuperação tributária, créditos PIS COFINS, ICMS, planejamento",
        "publicado": True,
        "destaque": True,
    },
]

for data in artigos_data:
    cat_nome = data.pop("categoria_nome")
    cat = Categoria.objects.get(nome=cat_nome)
    data["categoria"] = cat
    slug = slugify(data["titulo"])[:200]
    Artigo.objects.update_or_create(
        slug=slug,
        defaults={**data, "meta_title": data["titulo"][:70], "meta_description": data["resumo"][:160]},
    )

print("→ Criando cases fictícios...")
cases_data = [
    {
        "titulo": "Recuperação de R$ 2,5M em créditos de PIS/COFINS",
        "cliente_ficticio": "Indústria Metalúrgica Alfa",
        "setor": "industria",
        "resumo": "Empresa do setor metalúrgico com faturamento de R$ 80M/ano recuperou créditos de PIS/COFINS sobre insumos essenciais (energia, fretes, matérias-primas).",
        "problema": "A empresa pagava PIS/COFINS sobre todas as compras sem aproveitar créditos sobre insumos definidos pelo STJ (Tema 779). Muitos desses créditos vinham sendo apropriados de forma errada há anos.",
        "solucao": "Mapeamos todos os custos operacionais da empresa, identificamos quais se enquadravam como insumos essenciais, e preparamos pedido administrativo de restituição dos últimos 5 anos. Quando o pedido foi indeferido, ajuizamos ação judicial com pedido de tutela antecipada.",
        "resultado": "Recuperamos R$ 2,5M em créditos de PIS/COFINS dos últimos 5 anos, compensados diretamente na apuração mensal.",
        "resultado_numero": "R$ 2,5M recuperados",
        "duracao": "8 meses",
        "publicado": True,
        "destaque": True,
    },
    {
        "titulo": "Anulação de auto de infração de R$ 1,8M",
        "cliente_ficticio": "Grupo Varejo Beta",
        "setor": "comercio",
        "resumo": "Auto de infração lavrado pela Receita Federal por suposta omissão de receitas foi totalmente anulado por vício formal no procedimento fiscal.",
        "problema": "Receita Federal lavrou auto de infração de R$ 1,8M alegando omissão de receitas com base em cruzamento de dados eletrônicos. A empresa nunca recebeu intimação prévia válida.",
        "solucao": "Identificamos nulidade por falta de motivação adequada do auto (sem individualização dos valores por competência) e ausência de procedimento administrativo válido. Apresentamos impugnação administrativa robusta no CARF.",
        "resultado": "Auto de infração totalmente anulado. Nenhum valor foi pago. A empresa ainda recuperou custas processuais.",
        "resultado_numero": "R$ 1,8M economizados",
        "duracao": "14 meses",
        "publicado": True,
        "destaque": True,
    },
    {
        "titulo": "Due diligence tributária em aquisição de R$ 40M",
        "cliente_ficticio": "Holding Gama S.A.",
        "setor": "servicos",
        "resumo": "Due diligence tributária completa em operação de M&A identificou passivo oculto de R$ 3M, permitindo renegociação do preço de aquisição.",
        "problema": "Holding estava adquirindo empresa de serviços por R$ 40M. Auditoria tradicional não havia identificado contingências tributárias relevantes. Suspeita de passivo oculto surgiu em conversas informais.",
        "solucao": "Conduzimos due diligence tributária completa: análise de 5 anos de obrigações fiscais, auditoria de autos de infração em andamento, revisão de planejamento tributário atual e projeção de riscos com a Reforma Tributária.",
        "resultado": "Identificamos R$ 3M em passivos contingentes não declarados (autos de infração não contabilizados, discussões sobre ICMS-ST e créditos glosados). Cliente renegociou o preço em R$ 2,5M.",
        "resultado_numero": "R$ 2,5M economizados",
        "duracao": "3 meses",
        "publicado": True,
        "destaque": True,
    },
]

for data in cases_data:
    slug = slugify(data["titulo"])[:200]
    CaseEstudo.objects.update_or_create(
        slug=slug,
        defaults={**data, "meta_title": data["titulo"][:70], "meta_description": data["resumo"][:160]},
    )

print("\n✅ Seed completo!")
print(f"  Site: {site.domain}")
print(f"  Indicadores: {Numerico.objects.count()}")
print(f"  Depoimentos: {Depoimento.objects.count()}")
print(f"  Categorias: {Categoria.objects.count()}")
print(f"  Artigos: {Artigo.objects.count()}")
print(f"  Cases: {CaseEstudo.objects.count()}")
