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
]
