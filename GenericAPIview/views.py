from django.shortcuts import render
from . import serializer
from .models import CategoryModel, ProductModel 
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, get_object_or_404


class CategoryCreateView(GenericAPIView):
    serializer_class=serializer.CategorySerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(
            data={
                "message":"Category created successfully",
                "category":serializer.data
            },
            status=status.HTTP_201_CREATED
        )

class CategoryListView(GenericAPIView):
    queryset=CategoryModel.objects.all()
    serializer_class=serializer.CategorySerializer

    def get(self, request):
        queryset=self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        return Response(
            data={
                "message":"Category list fetched successfully",
                "count":queryset.count(),
                "categories":serializer.data
            },
            status=status.HTTP_200_OK
        )


class CategoryDetailView(GenericAPIView):
    serializer_class=serializer.CategorySerializer
    queryset=CategoryModel.objects.all()

    def get(self, request, pk):
        serializer = self.get_serializer(self.get_object())

        return Response(
            data={
                "message":"category detail fetched successfully",
                "category":serializer.data
            },
            status=status.HTTP_200_OK
        )


class CategoryUpdateView(GenericAPIView):
    serializer_class=serializer.CategorySerializer
    queryset=CategoryModel.objects.all()

    def put(self, request, pk):
        category = self.get_object()
        serializer = self.get_serializer(category, data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            data={
                "message":"category updated succcessfully",
                "category":serializer.data
            },
            status=status.HTTP_200_OK
        )


class CategoryDeleteView(GenericAPIView):
    queryset=CategoryModel.objects.all()

    def delete(self, request, pk):
        category = self.get_object()
        category.delete()

        return Response(
            data={
                "message":"category deleted successfully"
            },
            status=status.HTTP_200_OK
        )







class ProductCreateView(GenericAPIView):
    serializer_class=serializer.ProductSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            data={
                "message":"Product created successfully",
                "product":serializer.data
            },
            status=status.HTTP_201_CREATED
        )


class ProductListView(GenericAPIView):
    serializer_class=serializer.ProductSerializer
    queryset=ProductModel.objects.all()

    def get(self, request):
        queryset=self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        return Response(
            data={
                "message":"Preoduct list fetched",
                "count":queryset.count(),
                "products":serializer.data
            },
            status=status.HTTP_200_OK
        )


class ProductDetailView(GenericAPIView):
    serializer_class=serializer.ProductSerializer
    queryset=ProductModel.objects.all()

    def get(self, request, pk):
        serializer = self.get_serializer(self.get_object())

        return Response(
            data={
                "message":"product detail fetched successfully",
                "product":serializer.data
            },
            status=status.HTTP_200_OK
        )


class ProductUpdateView(GenericAPIView):
    serializer_class=serializer.ProductSerializer
    queryset=ProductModel.objects.all()

    def put(self, request, pk):
        serializer = self.get_serializer(self.get_object(), data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            data={
                "message":"product updated successfully",
                "product":serializer.data
            },
            status=status.HTTP_200_OK
        )


class ProductPartialUpdateView(GenericAPIView):
    serializer_class=serializer.ProductSerializer
    queryset=ProductModel.objects.all()

    def patch(self, request, pk):
        serializer = self.get_serializer(self.get_object(), data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            data={
                "message":"product partially updated",
                "product":serializer.data
            },
            status=status.HTTP_200_OK
        )        


class ProductDeleteView(GenericAPIView):
    queryset=ProductModel.objects.all()

    def delete(self, request, pk):
        product = self.get_object()
        product.delete()

        return Response(
            data={
                "message":"product deleted successfully"
            },
            status=status.HTTP_200_OK
        )
