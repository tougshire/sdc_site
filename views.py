import logging

import markdown
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, response
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.views.generic import DetailView, ListView
from touglates.templatetags import touglates_tags as touglates
from .models import Menu, Page, Rack

logger = logging.getLogger(__name__)


def home_page(request):
    try:
        page = Page.objects.filter(is_home=True).first()
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

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data["page_menus"] = Menu.objects.filter(
            menupage__page=self.get_object()
        )
        context_data["main_menus"] = Menu.objects.filter(level__gte=1000)

        return context_data


class RackView(DetailView):
    model = Rack
    template_name = "{}/rack.html".format(settings.SDC_SITE["TEMPLATE_DIR"])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data["page_menus"] = Menu.objects.filter(
            menupage__page=self.get_object()
        )
        context_data["main_menus"] = Menu.objects.filter(level__gte=1000)

        return context_data
