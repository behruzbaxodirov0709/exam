

from rest_framework.urls import path
from . import views
# from rest_framework.settings import  

urlpatterns = [
    path(route="create/category/", view=views.CategoryCreateView.as_view()),
    path(route="update/category/<int:pk>", view=views.CategoryUpdateView.as_view()),
    path(route="delete/category/<int:pk>", view=views.CategoryDeleteView.as_view()),
    path(route="detail/category/<int:pk>", view=views.CategoryDetailView.as_view()),
    path(route="list/category/", view=views.CategoryUpdateView.as_view()),

    path(route="create/product/", view=views.ProductCreateView.as_view()),
    path(route="detail/product/<int:pk>", view=views.ProductDetailView.as_view()),
    path(route="delete/product/<int:pk>", view=views.ProductDeleteView.as_view()),
    path(route="update/product/<int:pk>", view=views.ProductUpdateView.as_view()),
    path(route="create/product/", view=views.ProductCreateView.as_view()),
    path(route="list/product/", view=views.ProductListView.as_view()),
]


# urlpatterns += 