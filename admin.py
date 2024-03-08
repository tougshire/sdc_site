from django import forms
from django.contrib import admin
from .models import (
    Article,
    RackArticle,
    Rack,
    Menu,
    Menuitem,
    MenuPage,
    Page,
    Section,
    Site,
    Tag,
)


class RackArticleInline(admin.TabularInline):
    model = RackArticle
    extra = 0


class RackInline(admin.TabularInline):
    model = Rack
    extra = 0


class MenuitemInline(admin.TabularInline):
    model = Menuitem
    extra = 0


class MenuPageInline(admin.TabularInline):
    model = MenuPage
    extra = 0


class SectionInline(admin.TabularInline):
    model = Section
    extra = 0


class ArticleInline(admin.TabularInline):
    model = Article
    extra = 0


class RackAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    inlines = [
        RackArticleInline,
    ]


admin.site.register(RackArticle)

admin.site.register(Rack, RackAdmin)


class MenuAdmin(admin.ModelAdmin):
    inlines = [
        MenuitemInline,
    ]


admin.site.register(Menu, MenuAdmin)


class MenuitemModelForm(forms.ModelForm):
    page = forms.ModelChoiceField(
        Page.objects.all(),
        required=False,
        help_text="If selected, auto-fill href with a URL that points to the page (!will overwrite anything placed in the href field!)",
    )


class MenuitemAdmin(admin.ModelAdmin):
    form = MenuitemModelForm

    def save_model(self, request, obj, form, change):

        saved = super().save_model(request, obj, form, change)

        if form.cleaned_data["page"]:
            page = Page.objects.get(pk=form.cleaned_data["page"].pk)
            obj.href = "../" + page.slug
            if not form.cleaned_data["label"]:
                obj.label = page.title
            obj.save()

        return saved


admin.site.register(Menuitem, MenuitemAdmin)

admin.site.register(MenuPage)


class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    inlines = [
        SectionInline,
        MenuPageInline,
    ]


admin.site.register(Page, PageAdmin)


class SectionAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    inlines = [
        RackInline,
    ]


admin.site.register(Section, SectionAdmin)


class ArticleModelForm(forms.ModelForm):
    create_rack_to_section = forms.ModelChoiceField(
        Section.objects.all(),
        required=False,
        help_text="If selected, create a new rack for this article in the selected section",
    )


class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "updated_datetime"]
    form = ArticleModelForm
    prepopulated_fields = {"slug": ("title",)}
    inlines = [
        RackArticleInline,
    ]

    def save_model(self, request, obj, form, change):

        saved = super().save_model(request, obj, form, change)

        if form.cleaned_data["create_rack_to_section"]:
            rack = Rack.objects.create(
                name=obj.title,
                slug=obj.slug,
                section=form.cleaned_data["create_rack_to_section"],
            )
            RackArticle.objects.create(
                rack=rack,
                article=obj,
            )

        return saved


admin.site.register(Article, ArticleAdmin)


class SiteAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Site, SiteAdmin)
