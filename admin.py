from django.contrib import admin
from .models import (
    Article,
    ArticleTagory,
    Column,
    Menu,
    Menuitem,
    MenuPage,
    Page,
    Section,
    SectionColumn,
    Site,
    Tagory,
)


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Article)

admin.site.register(ArticleTagory)


class ColumnAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Column, ColumnAdmin)

admin.site.register(Menu)

admin.site.register(Menuitem)

admin.site.register(MenuPage)


class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Page, PageAdmin)


class SectionAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Section, SectionAdmin)

admin.site.register(SectionColumn)


class SiteAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Site, SiteAdmin)


class TagoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Tagory)
