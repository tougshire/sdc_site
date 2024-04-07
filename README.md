# SDC Site

A Django app CMS.  As of 2024, this is a limited and clunky CMS which might be useful as a starting point or an example for someone who wants to build their own.  On the other hand, it might fit your needs as is.

SDC is the initials of someone who I was working for when I started on this project

## Description


* It's not a blog.  Instead of automatically placing your article in a timeline, you place it where you want

## Getting Started

### Dependencies

* Touglates: [https://github.com/tougshire/touglates](https://github.com/tougshire/touglates).
* Django Filters Stoex: [https://github.com/tougshire/django_filters_stoex](https://github.com/tougshire/django_filters_stoex)
* Django Filters: [https://pypi.org/project/django-filter/](https://pypi.org/project/django-filter/)
* Django CKEditor 5: [https://pypi.org/project/django-ckeditor-5/](https://pypi.org/project/django-ckeditor-5/)
* Django Markdown: [https://pypi.org/project/django-markdown/](https://pypi.org/project/django-markdown/)
* This repository, SDC Site: [https://github.com/tougshire/sdc_site](https://github.com/tougshire/sdc_site)

### Installing

* Start a Django Project
* From your projecdt root folder (the one with manage.py in it), clone SDC Site, Django Filters Stoex, and Touglates using git
* * ex: `git clone https://github.com/tougshire/sdc_site`
* Install Django Filters and Django CKEditor 5 with pip
* * ex: pip install django-ckeditor-5

### Configuring

Follow the examples in the documentation for Django Filters and Django CKEDitor 5. You don't have to configure Django Markdown for this project, but it's included because Touglates requires it.

Your installed apps should look something like:

```
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "tougshire_auth.apps.TougshireAuthConfig",
    "touglates.apps.TouglatesConfig",
    "django_filters",
    "django_filters_stoex.apps.DjangoFiltersStoexConfig",
    "django_ckeditor_5",
    "sdc_site.apps.SdcSiteConfig",
]
```
* Add configuration settings for sdc_site.  Include the following code in your settings, and customize for your project:

```
SDC_SITE_AVAILABLE = {
    "default": {
        "SITE_NAME": "Toughire SDC_Site",
        "TEMPLATE_DIR": os.path.join("sdc_site", "default", ""),
        "STATIC_DIR": os.path.join("sdc_site", "default", ""),
        "BANNER_IMAGE": os.path.join("tougshire", "tougshire.banner.jpg"),
        "FOOTER_CONTENT": '<div class="footer" style="border:1px solid white; width:60%; margin:.5ex auto auto auto;"><br>Tougshire</div><br/> Suffolk, VA 23434',
        "COLORSCHEME": "green",
        "RECIPIENTS": ["tougshire@tougshire.com"],
        "head_lines": [
            '<!-- <a rel="me" href="https://assortedflotsam.com/@bnmng">Mastodon</a> -->'
        ],
        "keyed_head_lines": {
            "og_image": '<meta property="og:image" content="https://media.tougshire.com/tougshire/gallery/tougshireavatar.png" />',
            "og_image_alt": '<meta property="og:image:alt" content="The Tougshire Logo" />',
        },
    },
}

SDC_SITE = SDC_SITE_AVAILABLE["default"]

```


## Help

This is still in early phases and much more has to be done.

## Author

benjamin at tougshire.com

