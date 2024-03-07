from django.contrib import admin
from .models import (
    Article,
    Case,
    Menu,
    Menuitem,
    MenuPage,
    Page,
    Section,
    SectionCase,
    Site,
    Tag,
)


class MenuitemInline(admin.TabularInline):
    model = Menuitem
    extra = 0


class SectionInline(admin.TabularInline):
    model = Section
    extra = 0


class SectionCaseInline(admin.TabularInline):
    model = SectionCase
    extra = 0


class ArticleInline(admin.TabularInline):
    model = Article
    extra = 0


class CaseAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    inlines = [
        ArticleInline,
        SectionCaseInline,
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
        SectionCaseInline,
    ]


admin.site.register(Section, SectionAdmin)

admin.site.register(SectionCase)


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Article, ArticleAdmin)


class SiteAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Site, SiteAdmin)
