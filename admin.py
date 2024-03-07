from django import forms
from django.contrib import admin
from .models import (
    Article,
    CaseArticle,
    Case,
    Menu,
    Menuitem,
    MenuPage,
    Page,
    Section,
    Site,
    Tag,
)


class CaseArticleInline(admin.TabularInline):
    model = CaseArticle
    extra = 0


class CaseInline(admin.TabularInline):
    model = Case
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


class CaseAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    inlines = [
        CaseArticleInline,
    ]


admin.site.register(CaseArticle)

admin.site.register(Case, CaseAdmin)


class MenuAdmin(admin.ModelAdmin):
    inlines = [
        MenuitemInline,
    ]


admin.site.register(Menu, MenuAdmin)

admin.site.register(Menuitem)

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
        CaseInline,
    ]


admin.site.register(Section, SectionAdmin)


class ArticleModelForm(forms.ModelForm):
    create_case_to_section = forms.ModelChoiceField(
        Section.objects.all(),
        required=False,
        help_text="If selected, create a new case for this article in the selected section",
    )


class ArticleAdmin(admin.ModelAdmin):
    form = ArticleModelForm
    prepopulated_fields = {"slug": ("title",)}
    inlines = [
        CaseArticleInline,
    ]

    def save_model(self, request, obj, form, change):
        print("tp2437625", obj, obj.pk)

        saved = super().save_model(request, obj, form, change)

        print("tp2437626", obj, obj.pk)
        if form.cleaned_data["create_case_to_section"]:
            case = Case.objects.create(
                name=obj.title, section=form.cleaned_data["create_case_to_section"]
            )
            CaseArticle.objects.create(
                case=case,
                article=obj,
            )

        return saved


admin.site.register(Article, ArticleAdmin)


class SiteAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Site, SiteAdmin)
