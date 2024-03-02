from logging import Logger
import logging
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.conf import settings
from .models import Page
from django.http import HttpResponse, HttpResponseRedirect, response

logger = logging.getLogger(__name__)


def home_page(request):
    try:
        page = Page.objects.first()
        if page.slug:
            return HttpResponseRedirect(reverse("sdc_site:page", args=[page.slug]))
        else:
            return PageView(page.id)
    except Exception as e:
        logger.error(e)
        return HttpResponse("Error retrieving the page")


class PageView(DetailView):
    model = Page
    template_name = "{}/page.html".format(settings.SDC_SITE["TEMPLATE_DIR"])

    # def get_context_data(self, **kwargs):
    #     print(
    #         "tp2431646", self.object.menupage_set.all().first().menu.menuitem_set.all()
    #     )
    #     return super().get_context_data(**kwargs)
