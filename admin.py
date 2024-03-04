from django.contrib import admin
from .models import (
    Article,
    ArticleTagory,
    Column,
    Menu,
    Menuitem,
    MenuPage,
    Page,
    Segment,
    Section,
    SectionColumn,
    Site,
    Tagory,
)


class MenuitemInline(admin.TabularInline):
    model = Menuitem
    extra = 0


class SectionInline(admin.TabularInline):
    model = Section
    extra = 0


class SectionColumnInline(admin.TabularInline):
    model = SectionColumn
    extra = 0


class SegmentInline(admin.TabularInline):
    model = Segment
    extra = 0


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Article, ArticleAdmin)


admin.site.register(ArticleTagory)


class ColumnAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    inlines = [
        SegmentInline,
        SectionColumnInline,
    ]


admin.site.register(Column, ColumnAdmin)


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
        SectionColumnInline,
    ]


admin.site.register(Section, SectionAdmin)

admin.site.register(SectionColumn)


admin.site.register(Segment)


class SiteAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Site, SiteAdmin)


class TagoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Tagory)
