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

admin.site.register(Article)

admin.site.register(ArticleTagory)

admin.site.register(Column)

admin.site.register(Menu)

admin.site.register(Menuitem)

admin.site.register(MenuPage)

admin.site.register(Page)

admin.site.register(Section)

admin.site.register(SectionColumn)

admin.site.register(Site)

admin.site.register(Tagory)
