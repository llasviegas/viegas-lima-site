from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Lead
from .forms import LeadForm


def contato(request):
    if request.method == "POST":
        form = LeadForm(request.POST)
        if form.is_valid():
            lead = form.save(commit=False)
            # Captura IP
            x_forwarded = request.META.get("HTTP_X_FORWARDED_FOR")
            lead.ip_origem = x_forwarded.split(",")[0] if x_forwarded else request.META.get("REMOTE_ADDR")
            lead.save()
            messages.success(request, "Recebemos seu contato! Retornaremos em até 1 dia útil.")
            return redirect("leads:obrigado")
    else:
        form = LeadForm()
    return render(request, "leads/contato.html", {
        "form": form,
        "meta_title": "Contato | Viegas & Lima",
        "meta_description": "Entre em contato com a Viegas & Lima Advocacia. Consultoria tributária e jurídica estratégica.",
    })


def obrigado(request):
    return render(request, "leads/obrigado.html", {
        "meta_title": "Mensagem enviada | Viegas & Lima",
        "meta_description": "Recebemos sua mensagem.",
    })
