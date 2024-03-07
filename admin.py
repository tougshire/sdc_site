from django.contrib import admin
from .models import (
    Column,
    Menu,
    Menuitem,
    MenuPage,
    Page,
    Segment,
    Section,
    SectionColumn,
    Site,
    Tag,
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


class SegmentAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Segment, SegmentAdmin)


class SiteAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Site, SiteAdmin)
