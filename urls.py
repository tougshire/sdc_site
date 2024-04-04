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
    path("rack/", views.RackList.as_view(), name="rack-list"),
    path(
        "rack/<int:pk>/",
        views.RackView.as_view(),
        name="rack",
    ),
    path(
        "rack/<slug:slug>/",
        views.RackView.as_view(),
        name="rack",
    ),
    path("rack/create/", views.RackCreate.as_view(), name="rack-create"),
    path("rack/update/<int:pk>/", views.RackUpdate.as_view(), name="rack-update"),
    path("rack/delete/<int:pk>/", views.RackDelete.as_view(), name="rack-delete"),
    path("rack/popup/", views.RackCreate.as_view(), name="rack-popup"),
    path("rack/detail/<int:pk>/", views.RackDetail.as_view(), name="rack-detail"),
    path("article/", views.ArticleList.as_view(), name="article-list"),
    path(
        "article/<int:pk>/",
        views.ArticleView.as_view(),
        name="article",
    ),
    path(
        "article/<slug:slug>/",
        views.ArticleView.as_view(),
        name="article",
    ),
    path("article/create/", views.ArticleCreate.as_view(), name="article-create"),
    path(
        "article/update/<int:pk>/", views.ArticleUpdate.as_view(), name="article-update"
    ),
    path(
        "article/delete/<int:pk>/", views.ArticleDelete.as_view(), name="article-delete"
    ),
    path(
        "article/detail/<int:pk>/", views.ArticleDetail.as_view(), name="article-detail"
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
