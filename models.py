from datetime import date
from django.db import models
from django.conf import settings


class Page(models.Model):
    title = models.CharField(
        "title",
        blank=True,
        max_length=100,
        help_text="The title of the page. to be displayed (can be blank)",
    )
    show_title = models.BooleanField(
        "show title",
        default=True,
        help_text="If the title should be shown (if not blank)",
    )
    slug = models.SlugField(
        "name/slug",
        max_length=100,
        unique=True,
        help_text="The name or slug for use in URLs and within the application (must be unique and conform to slug standards)",
    )

    is_home = models.BooleanField(
        "is home page", default=False, help_text="If this is the home page"
    )
    order = models.IntegerField(
        "order",
        default=0,
        help_text="The order that the page would appear in a list",
    )
    display = models.CharField(
        "display",
        max_length=2,
        choices=[("Y", "Normal"), ("H", "Hide from Menus"), ("N", "Do not display")],
        default="Y",
        help_text="How the page should be displayed",
    )

    def __str__(self):
        return self.slug

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
    title = models.CharField(
        "title",
        blank=True,
        max_length=100,
        help_text="The title of the page. to be displayed (can be blank)",
    )
    show_title = models.BooleanField(
        "show title",
        default=True,
        help_text="If the title should be shown (if not blank)",
    )
    slug = models.SlugField(
        "name/slug",
        max_length=100,
        unique=True,
        help_text="The name or slug for use in URLs and within the application (must be unique and conform to slug standards)",
    )
    order = models.IntegerField(
        "order",
        default=0,
        help_text="The order that the section should appear on the page",
    )
    content_before_racks = models.TextField(
        blank=True,
        help_text="content to be displayed before the racks",
    )
    content_after_racks = models.TextField(
        blank=True,
        help_text="content to be displayed after the racks",
    )
    display = models.CharField(
        "display",
        max_length=2,
        choices=[("Y", "Normal"), ("P", "Preview Only"), ("N", "Do not display")],
        default="Y",
        help_text="How the section should be displayed",
    )

    def __str__(self):
        return '"{}" on page "{}"'.format(
            self.title if self.title > "" else self.slug, self.page
        )

    class Meta:
        ordering = ("page", "order")


class Rack(models.Model):
    section = models.ForeignKey(
        Section,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        help_text="The section to which the rack belongs",
    )
    title = models.CharField(
        "title",
        blank=True,
        max_length=100,
        help_text="The title of the rack to be displayed (can be blank)",
    )
    show_title = models.BooleanField(
        "show title",
        default=True,
        help_text="If the title should be shown (if not blank)",
    )
    slug = models.SlugField(
        "name/slug",
        max_length=100,
        unique=True,
        help_text="The name or slug for use in URLs and within the application (must be unique and conform to slug standards)",
    )
    width = models.IntegerField(
        "width",
        default=1,
        help_text="The width of the rack in multiples of how big it is compared to the narrowest rack",
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
        help_text="What article meta information should be shown for aticles in racks",
    )
    content_before_articles = models.CharField(
        "content before articles",
        max_length=255,
        blank=True,
        help_text="The content of the rack before any included articles",
    )

    content_after_articles = models.CharField(
        "content after articles",
        max_length=255,
        blank=True,
        help_text="The content of the rack after any included articles",
    )
    preview_for = models.ForeignKey(
        "Rack",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        help_text="The target rack if this rack is a preview for another.  The intent in this case is for you to fill out content before article",
    )
    order = models.IntegerField(
        "order",
        default=0,
        help_text="A number used for ordering of the rack in a section",
    )
    display = models.CharField(
        "display",
        max_length=2,
        choices=[
            ("Y", "Normal"),
            ("P", "Preview Only"),
            ("H", "Hide from sections"),
            ("N", "Do not display"),
        ],
        default="Y",
        help_text="How the rack should be displayed. Racks that are hidden from sections may still be displayed independently",
    )

    def __str__(self):

        return '"{}" in section "{}"'.format(
            self.title if self.title > "" else self.slug, self.section
        )

    class Meta:
        ordering = (
            "section",
            "order",
        )


class Document(models.Model):
    title = models.CharField(
        "title",
        max_length=100,
        blank=True,
        help_text="The title to be displayed with document.  It may or may not correspond to anything in the document itself. (can be blank)",
    )
    show_title = models.BooleanField(
        "show title",
        default=True,
        help_text="If the title should be shown (if not blank)",
    )
    slug = models.SlugField(
        "name/slug",
        max_length=100,
        unique=True,
        blank=True,
        help_text="The name or slug for use in URLs and within the application (must be unique and conform to slug standards)",
    )

    doc_file = models.FileField(
        upload_to="documents", help_text="The file to be uploaded"
    )

    def __str__(self):
        return (
            self.title
            if self.title > ""
            else self.slug if self.slug > "" else str(self.pk)
        )


class Article(models.Model):
    title = models.CharField(
        "title", max_length=100, help_text="The name of the article."
    )
    show_title = models.BooleanField(
        "show title",
        default=True,
        help_text="If the title should be shown (if not blank)",
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL
    )
    slug = models.SlugField(
        "name/slug",
        max_length=100,
        unique=True,
        help_text="The name or slug for use in URLs and within the application (must be unique and conform to slug standards)",
    )
    section = models.ForeignKey(
        Section,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        help_text="The section to which the article belongs if directly attached to a section",
    )
    width = models.IntegerField(
        "width",
        default=1,
        help_text="For section display, the width of the article in multiples of how big it is compared to the narrowest article in the section",
    )

    iframe_document = models.ForeignKey(
        Document,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        help_text="If selected, the document to be displayed in the iframe.  This will take precedence over anything entered in the iframe source field",
    )
    iframe_src = models.CharField(
        "iframe source",
        max_length=255,
        blank=True,
        help_text="If an iframe is to be displayed, the URL of an approved iframe source (must be listed in settings), optionally followed by a css height value",
    )
    iframe_height = models.CharField(
        "iframe height",
        max_length=20,
        blank=True,
        help_text="The height of the iframe using css height syntax.  Blank to use values set in stylesheets",
    )
    content = models.TextField(
        blank=True,
        help_text="The content of the article",
    )
    preview_for = models.ForeignKey(
        "Rack",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        help_text="The target rack if this rack is a preview for another.  The intent in this case is for you to fill out content before article",
    )
    can_contain_articles = models.BooleanField(
        "Can Contain Articles",
        default=False,
        help_text="If this article can contain other articles",
    )
    show_contained_article_meta = models.IntegerField(
        "show article meta",
        choices=[
            (0, "None"),
            (1, "Author"),
            (2, "Publish Date"),
            (3, "Author and Date"),
        ],
        default=0,
        help_text="What article meta information should be shown for aticles in racks",
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
        help_text="The published date, which can be filled in by the editors.  Used for sorting when more than one article is in a rack.",
    )
    display = models.CharField(
        "display",
        max_length=2,
        choices=[
            ("Y", "Normal"),
            ("P", "Preview Only"),
            ("H", "Hide from Racks"),
            ("N", "Do not display"),
        ],
        default="Y",
        help_text="How the section should be displayed.  If hidden from racks, the article may still be found by other means",
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("-publish_date", "title")


# class Article(models.Model):
#     title = models.CharField(
#         "title", max_length=100, help_text="The name of the article."
#     )
#     author = models.ForeignKey(
#         settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL
#     )
#     slug = models.SlugField(
#         "name/slug",
#         max_length=100,
#         unique=True,
#         help_text="The name or slug for use in URLs and within the application (must be unique and conform to slug standards)",
#     )

#     iframe_document = models.ForeignKey(
#         Document,
#         blank=True,
#         null=True,
#         on_delete=models.SET_NULL,
#         help_text="If selected, the document to be displayed in the iframe.  This will take precedence over anything entered in the iframe source field",
#     )
#     iframe_src = models.CharField(
#         "iframe source",
#         max_length=255,
#         blank=True,
#         help_text="If an iframe is to be displayed, the URL of an approved iframe source (must be listed in settings), optionally followed by a css height value",
#     )
#     iframe_height = models.CharField(
#         "iframe height",
#         max_length=20,
#         blank=True,
#         help_text="The height of the iframe using css height syntax.  Blank to use values set in stylesheets",
#     )
#     content_classes = models.CharField(
#         max_length=255,
#         blank=True,
#         default="article-content uldoc",
#         help_text="HTML classes to be applied to the content (default: article-content uldoc)",
#     )
#     content = models.TextField(
#         blank=True,
#         help_text="The content of the article.  Expected to usually include an iframe or series of iframes",
#     )
#     created_datetime = models.DateTimeField(
#         "date/time created",
#         auto_now_add=True,
#         help_text="The date/time that this article was created",
#     )
#     updated_datetime = models.DateTimeField(
#         "date/time updated",
#         auto_now=True,
#         help_text="The date/time that this article was updated",
#     )
#     publish_date = models.DateField(
#         "published",
#         default=date.today,
#         help_text="The published date, which can be filled in by the editors.  Used for sorting when more than one article is in a rack.",
#     )
#     display = models.CharField(
#         "display",
#         max_length=2,
#         choices=[
#             ("Y", "Normal"),
#             ("P", "Preview Only"),
#             ("H", "Hide from Racks"),
#             ("N", "Do not display"),
#         ],
#         default="Y",
#         help_text="How the section should be displayed.  If hidden from racks, the article may still be found by other means",
#     )

#     def __str__(self):
#         return self.title

#     class Meta:
#         ordering = ("-publish_date", "title")


class RackArticle(models.Model):
    rack = models.ForeignKey(
        Rack,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        help_text="The rack that holds the article",
    )
    container = models.ForeignKey(
        Article,
        blank=True,
        null=True,
        limit_choices_to={"can_contain_articles": True},
        on_delete=models.SET_NULL,
        help_text="The container article that holds the target article",
        related_name="to_target_article",
    )
    article = models.ForeignKey(
        Article,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        help_text="The article held by the containing article",
        related_name="to_containing_article",
    )
    order = models.IntegerField(
        "order",
        default=0,
        help_text="A number used to order the articles, overriding the default",
    )

    def __str__(self):
        return '"{}" in rack "{}"'.format(self.article, self.rack)

    class Meta:
        ordering = ("rack", "order", "article")


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
    level = models.IntegerField(
        "level",
        default=0,
        help_text="A number, like an id (but not unique enforced), which can be used for the page to indentify the menu. Use of 1000 for the main menu is recommended",
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("-level",)


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
        return '"{}" on page "{}"'.format(self.menu, self.page)
