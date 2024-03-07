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
    ]


admin.site.register(Page, PageAdmin)


class SectionAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    inlines = [
        CaseInline,
    ]


admin.site.register(Section, SectionAdmin)


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Article, ArticleAdmin)


class SiteAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Site, SiteAdmin)
