

from rest_framework.urls import path
from . import views

urlpatterns = [
    path(route="category/create/", view=views.CategoryCreateView.as_view()),
    path(route="category/update/<int:pk>", view=views.CategoryUpdateView.as_view()),
    path(route="category/delete/<int:pk>", view=views.CategoryDeleteView.as_view()),
    path(route="category/detail/<int:pk>", view=views.CategoryDetailView.as_view()),
    path(route="category/list/", view=views.CategoryListView.as_view()),

    path(route="product/create/", view=views.ProductCreateView.as_view()),
    path(route="product/detail/<int:pk>", view=views.ProductDetailView.as_view()),
    path(route="product/delete/<int:pk>", view=views.ProductDeleteView.as_view()),
    path(route="product/update/<int:pk>", view=views.ProductUpdateView.as_view()),
    path(route="product/partial-update/<int:pk>", view=views.ProductPartialUpdateView.as_view()),
    path(route="product/list/", view=views.ProductListView.as_view())
]