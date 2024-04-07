from django.db.models.query import QuerySet
from django_filters_stoex.views import FilterView
from django.contrib.auth.mixins import PermissionRequiredMixin

import logging

import markdown
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, response
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from django_filters_stoex.forms import (
    CSVOptionForm,
    FilterstoreRetrieveForm,
    FilterstoreSaveForm,
)
from sdc_site.filterset import ArticleFilter, RackFilter
from sdc_site.forms import (
    ArticleForm,
    ArticleHangerFormset,
    PageForm,
    PageSectionFormset,
    RackForm,
    RackHangerFormset,
    SectionForm,
    SectionRackFormset,
)
from touglates.templatetags import touglates_tags as touglates
from .models import Article, Menu, Page, Rack, Section

logger = logging.getLogger(__name__)


def get_modelfields_labels(model):
    fields = model._meta.get_fields()
    labels = {}

    for field in fields:
        try:
            labels[field.name] = field.verbose_name
        except:
            try:
                labels[field.name] = field.name.replace("_", " ")
            except:
                pass

    return labels


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


class PageCreate(CreateView):
    model = Page
    form_class = PageForm
    template_name = "sdc_site/edit/page_create.html"

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        formsetclasses = {
            "sections": PageSectionFormset,
        }

        for formsetkey, formsetclass in formsetclasses.items():
            if self.request.POST:
                context_data[formsetkey] = formsetclass(self.request.POST)
            else:
                context_data[formsetkey] = formsetclass()

        return context_data

    def form_valid(self, form):
        response = super().form_valid(form)

        self.object = form.save(commit=False)

        formsetclasses = {
            "sections": PageSectionFormset,
        }
        formsetdata = {}
        formsets_valid = True
        for formsetkey, formsetclass in formsetclasses.items():
            if self.request.POST:
                formsetdata[formsetkey] = formsetclass(
                    self.request.POST, instance=self.object
                )
            else:
                formsetdata[formsetkey] = formsetclass(instance=self.object)

            if (formsetdata[formsetkey]).is_valid():
                formsetdata[formsetkey].save()
            else:
                logger.critical(formsetdata[formsetkey].errors)
                for err in formsetdata[formsetkey].errors:
                    form.add_error(None, err)
                    for formsetform in formsetdata[formsetkey].forms:
                        for err in formsetform.errors:
                            form.add_error(None, err)
                formsets_valid = False

        if not formsets_valid:
            return self.form_invalid(form)

        return response

    def get_success_url(self):
        return reverse("sdc_site:page-detail", kwargs={"pk": self.object.pk})


class PageUpdate(UpdateView):
    model = Page
    form_class = PageForm
    template_name = "sdc_site/edit/page_update.html"

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        formsetclasses = {
            "sections": PageSectionFormset,
        }

        for formsetkey, formsetclass in formsetclasses.items():
            if self.request.POST:
                context_data[formsetkey] = formsetclass(
                    self.request.POST, instance=self.object
                )
            else:
                context_data[formsetkey] = formsetclass(instance=self.object)

        return context_data

    def form_valid(self, form):

        response = super().form_valid(form)

        self.object = form.save(commit=False)

        formsetclasses = {
            "sections": PageSectionFormset,
        }
        formsetdata = {}
        formsets_valid = True
        for formsetkey, formsetclass in formsetclasses.items():
            if self.request.POST:
                formsetdata[formsetkey] = formsetclass(
                    self.request.POST, instance=self.object
                )
            else:
                formsetdata[formsetkey] = formsetclass(instance=self.object)

            if (formsetdata[formsetkey]).is_valid():
                formsetdata[formsetkey].save()
            else:
                logger.critical(formsetdata[formsetkey].errors)
                for err in formsetdata[formsetkey].errors:
                    form.add_error(None, err)
                    for formsetform in formsetdata[formsetkey].forms:
                        for err in formsetform.errors:
                            form.add_error(None, err)
                formsets_valid = False

        if not formsets_valid:
            return self.form_invalid(form)

        return response

    def get_success_url(self):
        return reverse("sdc_site:page-detail", kwargs={"pk": self.object.pk})


class PageDetail(DetailView):
    model = Page
    template_name = "sdc_site/edit/page_detail.html"

    def get_context_data(self, **kwargs):

        context_data = super().get_context_data(**kwargs)

        context_data["object_labels"] = get_modelfields_labels(Page)

        return context_data


class PageDelete(DeleteView):
    model = Page
    template_name = "sdc_site/edit/page_confirm_delete.html"

    def get_context_data(self, *args, **kwargs):

        context_data = super().get_context_data(*args, **kwargs)

        context_data["object_labels"] = get_modelfields_labels(Page)

    def get_success_url(self):
        return reverse("sdc_site:page-list")


class PageList(PermissionRequiredMixin, ListView):
    model = Page
    permission_required = "sdc_site.view_page"
    template_name = "sdc_site/edit/page_list.html"

    def get_context_data(self, *args, **kwargs):

        context_data = super().get_context_data(*args, **kwargs)

        context_data["object_labels"] = get_modelfields_labels(Page)

        context_data["count"] = self.object_list.count()

        return context_data


class PageView(DetailView):
    model = Page
    template_name = "{}/page.html".format(settings.SDC_SITE["TEMPLATE_DIR"])

    def get_context_data(self, **kwargs):

        context_data = super().get_context_data(**kwargs)

        context_data["page_menus"] = Menu.objects.filter(
            menupage__page=self.get_object()
        )
        context_data["main_menus"] = Menu.objects.filter(level__gte=1000)

        context_data["base_url"] = self.request.build_absolute_uri("/")

        return context_data


class RackView(DetailView):
    model = Rack
    template_name = "sdc_site/edit/{}/rack.html".format(
        settings.SDC_SITE["TEMPLATE_DIR"]
    )

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data["main_menus"] = Menu.objects.filter(level__gte=1000)

        context_data["base_url"] = self.request.build_absolute_uri("/")

        return context_data


class ArticleCreate(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = "sdc_site/edit/article_create.html"

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        formsetclasses = {
            "hangers": ArticleHangerFormset,
        }

        for formsetkey, formsetclass in formsetclasses.items():
            if self.request.POST:
                context_data[formsetkey] = formsetclass(self.request.POST)
            else:
                context_data[formsetkey] = formsetclass()

        return context_data

    def form_valid(self, form):
        response = super().form_valid(form)

        self.object = form.save(commit=False)

        formsetclasses = {
            "hangers": ArticleHangerFormset,
        }
        formsetdata = {}
        formsets_valid = True
        for formsetkey, formsetclass in formsetclasses.items():
            if self.request.POST:
                formsetdata[formsetkey] = formsetclass(
                    self.request.POST, instance=self.object
                )
            else:
                formsetdata[formsetkey] = formsetclass(instance=self.object)

            if (formsetdata[formsetkey]).is_valid():
                formsetdata[formsetkey].save()
            else:
                logger.critical(formsetdata[formsetkey].errors)
                for err in formsetdata[formsetkey].errors:
                    form.add_error(None, err)
                    for formsetform in formsetdata[formsetkey].forms:
                        for err in formsetform.errors:
                            form.add_error(None, err)
                formsets_valid = False

        if not formsets_valid:
            return self.form_invalid(form)

        return response

    def get_success_url(self):
        return reverse("sdc_site:article-detail", kwargs={"pk": self.object.pk})


class ArticleUpdate(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = "sdc_site/edit/article_update.html"

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        formsetclasses = {
            "hangers": ArticleHangerFormset,
        }

        for formsetkey, formsetclass in formsetclasses.items():
            if self.request.POST:
                context_data[formsetkey] = formsetclass(
                    self.request.POST, instance=self.object
                )
            else:
                context_data[formsetkey] = formsetclass(instance=self.object)

        return context_data

    def form_valid(self, form):

        response = super().form_valid(form)

        self.object = form.save(commit=False)

        formsetclasses = {
            "hangers": ArticleHangerFormset,
        }
        formsetdata = {}
        formsets_valid = True
        for formsetkey, formsetclass in formsetclasses.items():
            if self.request.POST:
                formsetdata[formsetkey] = formsetclass(
                    self.request.POST, instance=self.object
                )
            else:
                formsetdata[formsetkey] = formsetclass(instance=self.object)

            if (formsetdata[formsetkey]).is_valid():
                formsetdata[formsetkey].save()
            else:
                logger.critical(formsetdata[formsetkey].errors)
                for err in formsetdata[formsetkey].errors:
                    form.add_error(None, err)
                    for formsetform in formsetdata[formsetkey].forms:
                        for err in formsetform.errors:
                            form.add_error(None, err)
                formsets_valid = False

        if not formsets_valid:
            return self.form_invalid(form)

        return response

    def get_success_url(self):
        return reverse("sdc_site:article-detail", kwargs={"pk": self.object.pk})


class ArticleDetail(DetailView):
    model = Article
    template_name = "sdc_site/edit/article_detail.html"

    def get_context_data(self, **kwargs):

        context_data = super().get_context_data(**kwargs)

        context_data["object_labels"] = get_modelfields_labels(Page)

        return context_data


class ArticleDelete(DeleteView):
    model = Article
    template_name = "sdc_site/edit/article_confirm_delete.html"

    def get_success_url(self):
        return reverse("sdc_site:article-list")


class ArticleList(PermissionRequiredMixin, FilterView):
    model = Article
    permission_required = "sdc_site.view_article"
    filterset_class = ArticleFilter
    filterstore_urlname = "sdc_site:article-filterstore"
    template_name = "sdc_site/edit/article_filter.html"

    def get_context_data(self, *args, **kwargs):

        context_data = super().get_context_data(*args, **kwargs)

        context_data["filterstore_retrieve"] = FilterstoreRetrieveForm()
        context_data["filterstore_save"] = FilterstoreSaveForm()
        context_data["as_csv"] = CSVOptionForm()

        context_data["object_labels"] = get_modelfields_labels(Page)

        context_data["count"] = self.object_list.count()

        return context_data


class ArticleView(DetailView):
    model = Article
    template_name = "{}/article.html".format(settings.SDC_SITE["TEMPLATE_DIR"])


class RackCreate(CreateView):
    model = Rack
    form_class = RackForm
    template_name = "sdc_site/edit/rack_create.html"

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        formsetclasses = {
            "hangers": RackHangerFormset,
        }

        for formsetkey, formsetclass in formsetclasses.items():
            if self.request.POST:
                context_data[formsetkey] = formsetclass(self.request.POST)
            else:
                context_data[formsetkey] = formsetclass()

        return context_data

    def form_valid(self, form):
        response = super().form_valid(form)

        self.object = form.save(commit=False)

        formsetclasses = {
            "hangers": RackHangerFormset,
        }
        formsetdata = {}
        formsets_valid = True
        for formsetkey, formsetclass in formsetclasses.items():
            if self.request.POST:
                formsetdata[formsetkey] = formsetclass(
                    self.request.POST, instance=self.object
                )
            else:
                formsetdata[formsetkey] = formsetclass(instance=self.object)

            if (formsetdata[formsetkey]).is_valid():
                formsetdata[formsetkey].save()
            else:
                logger.critical(formsetdata[formsetkey].errors)
                for err in formsetdata[formsetkey].errors:
                    form.add_error(None, err)
                    for formsetform in formsetdata[formsetkey].forms:
                        for err in formsetform.errors:
                            form.add_error(None, err)
                formsets_valid = False

        if not formsets_valid:
            return self.form_invalid(form)

        return response

    def get_success_url(self):
        return reverse("sdc_site:rack-detail", kwargs={"pk": self.object.pk})


class RackUpdate(UpdateView):
    model = Rack
    form_class = RackForm
    template_name = "sdc_site/edit/rack_update.html"

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        formsetclasses = {
            "hangers": RackHangerFormset,
        }

        for formsetkey, formsetclass in formsetclasses.items():
            if self.request.POST:
                context_data[formsetkey] = formsetclass(
                    self.request.POST, instance=self.object
                )
            else:
                context_data[formsetkey] = formsetclass(instance=self.object)

        return context_data

    def form_valid(self, form):

        response = super().form_valid(form)

        self.object = form.save(commit=False)

        formsetclasses = {
            "hangers": RackHangerFormset,
        }
        formsetdata = {}
        formsets_valid = True
        for formsetkey, formsetclass in formsetclasses.items():
            if self.request.POST:
                formsetdata[formsetkey] = formsetclass(
                    self.request.POST, instance=self.object
                )
            else:
                formsetdata[formsetkey] = formsetclass(instance=self.object)

            if (formsetdata[formsetkey]).is_valid():
                formsetdata[formsetkey].save()
            else:
                logger.critical(formsetdata[formsetkey].errors)
                for err in formsetdata[formsetkey].errors:
                    form.add_error(None, err)
                    for formsetform in formsetdata[formsetkey].forms:
                        for err in formsetform.errors:
                            form.add_error(None, err)
                formsets_valid = False

        if not formsets_valid:
            return self.form_invalid(form)

        return response

    def get_success_url(self):
        return reverse("sdc_site:rack-detail", kwargs={"pk": self.object.pk})


class RackDetail(DetailView):
    model = Rack
    template_name = "sdc_site/edit/rack_detail.html"


class RackDelete(DeleteView):
    model = Rack
    template_name = "sdc_site/edit/rack_confirm_delete.html"

    def get_success_url(self):
        return reverse("sdc_site:rack-list")


class RackList(PermissionRequiredMixin, FilterView):
    model = Rack
    permission_required = "sdc_site.view_rack"
    filterset_class = RackFilter
    filterstore_urlname = "sdc_site:rack-filterstore"
    template_name = "sdc_site/edit/rack_filter.html"

    def get_context_data(self, *args, **kwargs):

        context_data = super().get_context_data(*args, **kwargs)

        context_data["filterstore_retrieve"] = FilterstoreRetrieveForm()
        context_data["filterstore_save"] = FilterstoreSaveForm()
        context_data["as_csv"] = CSVOptionForm()

        context_data["object_labels"] = get_modelfields_labels(Page)

        context_data["count"] = self.object_list.count()

        return context_data


class SectionCreate(CreateView):
    model = Section
    form_class = SectionForm
    template_name = "sdc_site/edit/section_create.html"

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        formsetclasses = {
            "racks": SectionRackFormset,
        }

        for formsetkey, formsetclass in formsetclasses.items():
            if self.request.POST:
                context_data[formsetkey] = formsetclass(self.request.POST)
            else:
                context_data[formsetkey] = formsetclass()

        return context_data

    def form_valid(self, form):
        response = super().form_valid(form)

        self.object = form.save(commit=False)

        formsetclasses = {
            "racks": SectionRackFormset,
        }
        formsetdata = {}
        formsets_valid = True
        for formsetkey, formsetclass in formsetclasses.items():
            if self.request.POST:
                formsetdata[formsetkey] = formsetclass(
                    self.request.POST, instance=self.object
                )
            else:
                formsetdata[formsetkey] = formsetclass(instance=self.object)

            if (formsetdata[formsetkey]).is_valid():
                formsetdata[formsetkey].save()
            else:
                logger.critical(formsetdata[formsetkey].errors)
                for err in formsetdata[formsetkey].errors:
                    form.add_error(None, err)
                    for formsetform in formsetdata[formsetkey].forms:
                        for err in formsetform.errors:
                            form.add_error(None, err)
                formsets_valid = False

        if not formsets_valid:
            return self.form_invalid(form)

        return response

    def get_success_url(self):
        return reverse("sdc_site:section-detail", kwargs={"pk": self.object.pk})


class SectionUpdate(UpdateView):
    model = Section
    form_class = SectionForm
    template_name = "sdc_site/edit/section_update.html"

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        formsetclasses = {
            "racks": SectionRackFormset,
        }

        for formsetkey, formsetclass in formsetclasses.items():
            if self.request.POST:
                context_data[formsetkey] = formsetclass(
                    self.request.POST, instance=self.object
                )
            else:
                context_data[formsetkey] = formsetclass(instance=self.object)

        return context_data

    def form_valid(self, form):

        response = super().form_valid(form)

        self.object = form.save(commit=False)

        formsetclasses = {
            "racks": SectionRackFormset,
        }
        formsetdata = {}
        formsets_valid = True
        for formsetkey, formsetclass in formsetclasses.items():
            if self.request.POST:
                formsetdata[formsetkey] = formsetclass(
                    self.request.POST, instance=self.object
                )
            else:
                formsetdata[formsetkey] = formsetclass(instance=self.object)

            if (formsetdata[formsetkey]).is_valid():
                formsetdata[formsetkey].save()
            else:
                logger.critical(formsetdata[formsetkey].errors)
                for err in formsetdata[formsetkey].errors:
                    form.add_error(None, err)
                    for formsetform in formsetdata[formsetkey].forms:
                        for err in formsetform.errors:
                            form.add_error(None, err)
                formsets_valid = False

        if not formsets_valid:
            return self.form_invalid(form)

        return response

    def get_success_url(self):
        return reverse("sdc_site:section-detail", kwargs={"pk": self.object.pk})


class SectionDetail(DetailView):
    model = Section
    template_name = "sdc_site/edit/section_detail.html"


class SectionDelete(DeleteView):
    model = Section
    template_name = "sdc_site/edit/section_confirm_delete.html"

    def get_success_url(self):
        return reverse("sdc_site:section-list")

    def get_success_url(self):
        return reverse("sdc_site:section-list")


class SectionList(PermissionRequiredMixin, ListView):
    model = Section
    permission_required = "sdc_site.view_section"
    template_name = "sdc_site/edit/section_list.html"

    def get_context_data(self, *args, **kwargs):

        context_data = super().get_context_data(*args, **kwargs)

        context_data["object_labels"] = get_modelfields_labels(Page)

        context_data["count"] = self.object_list.count()

        return context_data
