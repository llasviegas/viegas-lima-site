from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site


def site_info(request):
    site = get_current_site(request)
    scheme = "https" if request.is_secure() else "http"
    return {
        "SITE_NAME": site.name,
        "SITE_DOMAIN": site.domain,
        "SITE_URL": f"{scheme}://{site.domain}",
        "WHATSAPP_NUMBER": getattr(settings, "DEFAULT_WHATSAPP", ""),
    }
