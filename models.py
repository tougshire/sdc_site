from datetime import date
from django.db import models


class Site(models.Model):
    name = models.CharField("name", max_length=100, help_text="The name of the site.")
    slug = models.SlugField(
        "slug", max_length=100, unique=True, help_text="The slug for use in URLs"
    )

    def __str__(self):
        return self.name


class Page(models.Model):
    site = models.ForeignKey(
        Site,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="The site to which this page belongs",
    )
    title = models.CharField(
        "title", max_length=100, help_text="The title of the page."
    )
    slug = models.SlugField(
        "slug", max_length=100, unique=True, help_text="The slug for use in URLs"
    )
    order = models.IntegerField(
        "order",
        default=0,
        help_text="The order that the page would appear in a list",
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("order", "title")


class Section(models.Model):
    page = models.ForeignKey(
        Page,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="The page to which this column belongs",
    )
    name = models.CharField(
        "name", max_length=100, help_text="The name of the section."
    )
    slug = models.SlugField(
        "slug", max_length=100, unique=True, help_text="The slug for use in URLs"
    )
    order = models.IntegerField(
        "order",
        default=0,
        help_text="The order that the section should appear on the page",
    )
    content_before = models.TextField(
        blank=True,
        help_text="content to be displayed above the columns",
    )
    content_after = models.TextField(
        blank=True,
        help_text="content to be displayed below the columns",
    )

    def __str__(self):
        return "{}:{}".format(self.page, self.name)

    class Meta:
        ordering = ("order", "name")


class Column(models.Model):
    name = models.CharField("name", max_length=100, help_text="The name of the column.")
    slug = models.SlugField(
        "slug", max_length=100, unique=True, help_text="The slug for use in URLs"
    )
    width = models.IntegerField(
        "width",
        default=1,
        help_text="The width of the column in multiples of how big it is compared to the narrowest column",
    )
    content = models.TextField(
        blank=True,
        help_text="The content of the column.  Expected to usually include an iframe or series of iframes",
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)


class SectionColumn(models.Model):
    section = models.ForeignKey(
        Section,
        on_delete=models.CASCADE,
        help_text="The section to which the column belongs",
    )
    column = models.ForeignKey(
        Column,
        on_delete=models.CASCADE,
        help_text="The column which appears in the section",
    )
    order = models.IntegerField(
        "order",
        default=0,
        help_text="The order that the section would appear on the page",
    )

    class Meta:
        ordering = ("section", "order")

    def __str__(self):
        return "{} on {}".format(self.column, self.section)


class Article(models.Model):
    page = models.ForeignKey(
        Page,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="The page to which this column belongs",
    )
    title = models.CharField(
        "name", max_length=100, help_text="The name of the column."
    )
    slug = models.SlugField(
        "slug", max_length=100, unique=True, help_text="The slug for use in URLs"
    )
    content = models.TextField(
        blank=True,
        help_text="The content of the article.",
    )
    order = models.IntegerField(
        "order",
        default=0,
        help_text="The order that the column should appear on the page",
    )
    width = models.IntegerField(
        "width",
        default=1,
        help_text="The width of the column in multiples of how big it is compared to the narrowest column",
    )
    when_created = models.DateTimeField(
        "created", auto_now_add=True, help_text="The date the article was created"
    )
    when_updated = models.DateTimeField(
        "updated", auto_now=True, help_text="The date the article was updated"
    )
    date_for_dateline = models.DateField(
        "date", default=date.today, help_text="The displayed date of the article"
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("-date_for_dateline", "-when_updated")


class Tagory(models.Model):
    name = models.CharField("name", max_length=100, help_text="The name of the tag.")
    slug = models.SlugField(
        "slug", max_length=100, unique=True, help_text="The slug for use in URLs"
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)


class ArticleTagory(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        help_text="The article to which the tag belongs",
    )
    tagory = models.ForeignKey(
        Tagory,
        on_delete=models.CASCADE,
        help_text="The tag to which the article belongs",
    )

    def __str__(self):
        return "{} tagged {}".format(self.article, self.tagory)

    class Meta:
        ordering = ("article", "tagory")


class Menu(models.Model):
    name = models.CharField(
        "name", max_length=30, blank=True, help_text="The label of this menu item"
    )

    def __str__(self):
        return self.name


class Menuitem(models.Model):
    menu = models.ForeignKey(
        Menu,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="The menu to which this item belongs",
    )
    href = models.CharField(
        "href",
        max_length=255,
        blank=True,
        help_text="The URL that this menu item points to",
    )
    label = models.CharField(
        "label", max_length=30, blank=True, help_text="The label of this menu item"
    )
    order = models.IntegerField(
        "order",
        help_text="The order that the item would appear in a menu",
    )

    def __str__(self):
        return self.label


class MenuPage(models.Model):
    menu = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE,
        help_text="The menu that is attached to this page",
    )
    page = models.ForeignKey(
        Page,
        on_delete=models.CASCADE,
        help_text="The page that this menu is attached to ",
    )

    def __str__(self):
        return "{} on {}".format(self.menu, self.page)
