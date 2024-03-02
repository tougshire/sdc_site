from django.conf import settings


def sdc_site(request):
    return {"sdc_site": settings.SDC_SITE}
