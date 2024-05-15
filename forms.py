import datetime
from django.conf import settings
from django.forms import ModelForm, SelectDateWidget, inlineformset_factory, Select
from django.urls import reverse_lazy
from .models import Article, Articlecomment, Sdcimage, Page, Rack, Hanger, Section
from django import forms
from touglates.widgets import TouglateRelatedSelect, SlugInput

# from django_c_keditor_5.widgets import C_KEditor5Widget


class ArticleForm(ModelForm):
    image_select = forms.ModelChoiceField(
        required=False,
        queryset=Sdcimage.objects.all(),
        to_field_name="markdown_code",
        widget=TouglateRelatedSelect(
            related_data={
                "model": "Sdcimage",
                "add_url": reverse_lazy("sdc_site:sdcimage-popup"),
            },
        ),
    )

    class Meta:
        model = Article
        fields = [
            "title",
            "show_title",
            "author",
            "slug",
            "iframe_document",
            "iframe_src",
            "iframe_height",
            "summary",
            "content",
            "if_summary_blank",
            "publish_date",
            "display",
            "featured_image",
        ]

        widgets = {
            "title": forms.TextInput(attrs={"class": "widthlong"}),
            "slug": SlugInput(
                slug_name="slug", input_name="title", attrs={"class": "widthlong"}
            ),
            "iframe_src": forms.TextInput(attrs={"class": "widthlong"}),
            "summary": forms.TextInput(attrs={"class": "widthlong"}),
            # "summary": C_KEditor5Widget(
            #     config_name="extends", attrs={"style": "width:100%;"}
            # ),
            "content": forms.Textarea(attrs={"class": "widthlong"}),
            # "content": C_KEditor5Widget(
            #     config_name="extends", attrs={"style": "width:100%;"}
            # ),
        }


class HangerForm(ModelForm):
    class Meta:
        fields = [
            "rack",
            "article",
            "order",
            "expiration_date",
        ]
        widgets = {
            "rack": TouglateRelatedSelect(
                related_data={
                    "model": "Rack",
                    "add_url": reverse_lazy("sdc_site:rack-popup"),
                }
            )
        }


class RackForm(ModelForm):
    class Meta:
        model = Rack
        fields = [
            "section",
            "title",
            "show_title",
            "slug",
            "width",
            "show_article_meta",
            "content_before_articles",
            "content_after_articles",
            "order",
            "display",
        ]
        widgets = {
            "title": forms.TextInput(attrs={"class": "widthlong"}),
            "slug": SlugInput(
                slug_name="slug", input_name="title", attrs={"class": "widthlong"}
            ),
        }


class SectionForm(ModelForm):
    class Meta:
        model = Section
        fields = [
            "page",
            "title",
            "show_title",
            "slug",
            "order",
            "content_before_racks",
            "content_after_racks",
            "display",
        ]
        widgets = {
            "title": forms.TextInput(attrs={"class": "widthlong"}),
            "slug": SlugInput(
                slug_name="slug", input_name="title", attrs={"class": "widthlong"}
            ),
        }


class PageForm(ModelForm):
    class Meta:
        model = Page
        fields = [
            "title",
            "show_title",
            "slug",
            "is_home",
            "order",
            "display",
        ]
        widgets = {
            "title": forms.TextInput(attrs={"class": "widthlong"}),
            "slug": SlugInput(
                slug_name="slug", input_name="title", attrs={"class": "widthlong"}
            ),
        }


class ArticlecommentForm(forms.ModelForm):
    class Meta:
        model = Articlecomment
        fields = ("name", "email", "content")


class SdcimageForm(forms.ModelForm):
    class Meta:
        model = Sdcimage
        fields = ("imagefile", "name", "alt_text", "title")


ArticleHangerFormset = inlineformset_factory(Article, Hanger, form=HangerForm, extra=10)
RackHangerFormset = inlineformset_factory(Rack, Hanger, form=HangerForm, extra=10)
PageSectionFormset = inlineformset_factory(Page, Section, form=SectionForm, extra=10)
SectionRackFormset = inlineformset_factory(Section, Rack, form=RackForm, extra=10)
