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
        help_text="The page to which this section belongs",
    )
    name = models.CharField(
        "name", max_length=100, help_text="The title of the section."
    )
    show_title = models.BooleanField(
        "show title",
        default=True,
        help_text="Show the title of the section ",
    )
    slug = models.SlugField(
        "slug", max_length=100, unique=True, help_text="The slug for use in URLs"
    )
    order = models.IntegerField(
        "order",
        default=0,
        help_text="The order that the section should appear on the page",
    )
    content_before_cases = models.TextField(
        blank=True,
        help_text="content to be displayed before the cases",
    )
    content_after_cases = models.TextField(
        blank=True,
        help_text="content to be displayed after the cases",
    )

    def __str__(self):
        return "{}:{}".format(self.page, self.name)

    class Meta:
        ordering = ("order", "name")


class Case(models.Model):
    section = models.ForeignKey(
        Section,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        help_text="The section to which the case belongs",
    )
    name = models.CharField("name", max_length=100, help_text="The name of the case.")
    slug = models.SlugField(
        "slug", max_length=100, unique=True, help_text="The slug for use in URLs"
    )
    width = models.IntegerField(
        "width",
        default=1,
        help_text="The width of the case in multiples of how big it is compared to the narrowest case",
    )
    show_article_meta = models.CharField(
        "show article meta",
        max_length=2,
        choices=[
            ("00", "None"),
            ("a0", "Author"),
            ("0d", "Publish Date"),
            ("ad", "Author and Date"),
        ],
        default="00",
        help_text="What article meta information should be shown for aticles in cases",
    )
    content_before_articles = models.CharField(
        max_length=255,
        blank=True,
        help_text="The content of the case before any included articles",
    )

    content_after_articles = models.CharField(
        max_length=255,
        blank=True,
        help_text="The content of the case after any included articles",
    )
    order = models.IntegerField(
        "order",
        default=0,
        help_text="A number used for ordering of the case in a section",
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = (
            "order",
            "name",
        )


class Article(models.Model):
    title = models.CharField(
        "title", max_length=100, help_text="The name of the article."
    )
    iframe_src = models.CharField(
        "iframe source",
        max_length=255,
        blank=True,
        help_text="If an iframe is to be displayed, the URL of an approved iframe source (must be listed in settings), optionally followed by a css height value",
    )
    content_classes = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        default="article-content uldoc",
        help_text="HTML classes to be applied to the content (default: article-content uldoc)",
    )
    content_format = models.CharField(
        max_length=12,
        choices=(
            ("markdown", "Markdown"),
            ("html", "HTML"),
            ("plaintext", "Plain Text"),
        ),
        default="markdown",
        help_text="The format used for rendering the content",
    )
    content = models.TextField(
        blank=True,
        help_text="The content of the article.  Expected to usually include an iframe or series of iframes",
    )
    order = models.IntegerField(
        "order",
        default=0,
        help_text="The order that the article would appear in the case",
    )
    created_datetime = models.DateTimeField(
        "date/time created",
        auto_now_add=True,
        help_text="The date/time that this article was created",
    )
    updated_datetime = models.DateTimeField(
        "date/time updated",
        auto_now=True,
        help_text="The date/time that this article was updated",
    )
    publish_date = models.DateField(
        "published",
        default=date.today,
        help_text="The published date, which can be filled in by the editors.  Used for sorting when more than one article is in a case.",
    )

    slug = models.SlugField(
        "slug",
        unique=True,
        max_length=100,
        help_text="The slug for use in URLs",
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("-publish_date", "title")


class CaseArticle(models.Model):
    case = models.ForeignKey(Case, blank=True, null=True, on_delete=models.SET_NULL)
    article = models.ForeignKey(
        Article, blank=True, null=True, on_delete=models.SET_NULL
    )


class Tag(models.Model):
    name = models.CharField("name", max_length=100, help_text="The name of the tag.")
    slug = models.SlugField(
        "slug", max_length=100, unique=True, help_text="The slug for use in URLs"
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)


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
