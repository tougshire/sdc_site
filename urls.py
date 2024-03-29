from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
from django.views.generic.base import RedirectView
from django.urls import path, reverse_lazy
from . import views

app_name = "sdc_site"

urlpatterns = [
    path("", RedirectView.as_view(url=reverse_lazy("sdc_site:homepage"))),
    path("homepage/", views.home_page, name="homepage"),
    path(
        "page/<int:pk>/",
        views.PageView.as_view(),
        name="page",
    ),
    path(
        "page/<slug:slug>/",
        views.PageView.as_view(),
        name="page",
    ),
    path(
        "article/<int:pk>/",
        views.RackView.as_view(),
        name="rack",
    ),
    path(
        "article/<slug:slug>/",
        views.RackView.as_view(),
        name="rack",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
