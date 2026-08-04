# Viegas & Lima Advocacia — Site Institucional v2

Site institucional Django com foco em **Direito Tributário Estratégico**.

## Stack

- **Backend**: Django 5.1.4 (Python 3.11)
- **Frontend**: Django templates + HTMX + Alpine.js
- **CSS**: Tailwind CDN (sem build step)
- **DB**: SQLite (dev) / Postgres (prod — Render)
- **Hospedagem**: Render Free Tier
- **Domínio**: viegaselima.com.br

## Setup local

```bash
python -m venv venv
source venv/Scripts/activate   # Windows
# source venv/bin/activate     # Linux/Mac
pip install -r requirements.txt

cp .env.example .env
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Acesse: http://localhost:8000

## Deploy (Render)

1. Crie Personal Access Token no GitHub (https://github.com/settings/tokens/new)
2. Push pro repo `viegas-lima/site`
3. Conecte o repo no Render (Blueprint detecta `render.yaml`)
4. Render provisiona Postgres + Web Service automaticamente
5. Aponta DNS no Hostinger pra Render

Ver `INSTRUCOES-PAT-GITHUB.md` para detalhes.

## Estrutura

```
apps/
├── core/          → Home, Sobre, Equipe
├── tributario/    → 5 sub-páginas tributário (carro-chefe)
├── empresarial/   → M&A, Contratos
├── civil/
├── trabalhista/
├── previdenciario/
├── familia/
├── blog/          → Artigos SEO
├── cases/         → Cases de sucesso
└── leads/         → Formulário de contato

vl_website/
├── settings.py
├── urls.py
├── wsgi.py
└── manage.py
```

## Conteúdo admin

- Acesse `/admin/`
- Cadastros:
  - **Configuração do Site** (telefone, WhatsApp, redes)
  - **Indicadores Numéricos** (150+ casos, R$ economizados)
  - **Depoimentos** (fictícios)
  - **Páginas Tributário**
  - **Artigos** (blog)
  - **Cases** (cases de sucesso)
  - **Leads** (formulário de contato)

## SEO

- Meta tags únicas por página
- Schema.org LegalService
- Sitemap.xml automático (`/sitemap.xml`)
- Robots.txt (`/robots.txt`)
- URLs amigáveis (sem query strings)
- HTML semântico

## Custos

**R$ 0/mês** (Render free tier + Tailwind CDN + HTMX CDN + Alpine CDN)

Domínio viegaselima.com.br já pago no Hostinger.

## Licença

Proprietary © Viegas & Lima Advocacia
