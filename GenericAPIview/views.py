from django.shortcuts import render
from . import serializer
from .models import CategoryModel, ProductModel 
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, get_object_or_404


class CategoryCreateView(GenericAPIView):
    def post(self, request):
        serializer_class=serializer.CategorySerializer
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
    def get(self, request):
        queryset=CategoryModel.objects.all()
        serializer_class=serializer.CategorySerializer

        serializer = self.get_serializer(self.get_queryset, many=True)

        return Response(
            data={
                "message":"Category list fetched successfully",
                "count":serializer.count(),
                "categories":serializer.data
            },
            status=status.HTTP_200_OK
        )


class CategoryDetailView(GenericAPIView):
    def get(self, reqeust, pk):
        serializer_class=serializer.CategorySerializer
        queryset=CategoryModel.objects.all()
        lookup_url_kwarg=pk

        serializer = self.get_serializer(self.get_object())

        return Response(
            data={
                "message":"category detail fetched successfully",
                "category":serializer.data
            },
            status=status.HTTP_200_OK
        )


class CategoryUpdateView(GenericAPIView):
    def put(self, request, pk):
        serializer_class=serializer.CategorySerializer
        lookup_url_kwarg=pk
        queryset=CategoryModel.objects.all()
        serializer = self.get_object()

        serializer = self.get_serializer(data=request.data)

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
    def delete(self, request, pk):
        lookup_url_kwarg=pk
        queryset=CategoryModel.objects.all()
        serializer = self.get_object()

        serializer.delete()

        return Response(
            data={
                "message":"category deleted successfully"
            },
            status=status.HTTP_200_OK
        )



class ProductCreateView(GenericAPIView):
    def post(self, request):
        serializer_class=serializer.ProductSerializer

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
    def get(self, request):
        serializer_class=serializer.ProductSerializer
        queryset=ProductModel.objects.all()

        serializer = self.get_serializer(many=True)

        return Response(
            data={
                "message":"Preoduct list fetched",
                "count":serializer.count(),
                "products":serializer.data
            },
            status=status.HTTP_200_OK
        )


class ProductDetailView(GenericAPIView):
    def get(self, request, pk):
        serializer_class=serializer.ProductSerializer
        queryset=ProductModel.objects.all()
        lookup_url_kwarg=pk

        serializer = self.get_object()

        return Response(
            data={
                "message":"product detail fetched successfully",
                "product":serializer.data
            },
            status=status.HTTP_200_OK
        )


class ProductUpdateView(GenericAPIView):
    def put(self, request, pk):
        serializer_class=serializer.ProductSerializer
        queryset=ProductModel.objects.all()
        lookup_url_kwarg=pk


        serializer = self.get_serializer(self.get_object())

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(
            data={
                "msg":"product updated",
                "product":serializer.data
            },
            status=status.HTTP_200_OK
        )


class ProductPartialUpdateView(GenericAPIView):
    def patch(self, request, pk):
        serializer_class=serializer.ProductSerializer
        queryset=ProductModel.objects.all()
        lookup_url_kwarg=pk


        serializer = self.get_serializer(self.get_object(), partial=True)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(
            data={
                "msg":"product partially updated",
                "product":serializer.data
            },
            status=status.HTTP_200_OK
        )        


class ProductDeleteView(GenericAPIView):
    def delete(self, request, pk):
        queryset=ProductModel.objects.all()
        lookup_url_kwarg=pk

        serializer = self.get_object()

        serializer.delete()

        return Response(
            data={
                "msg":"product deleted"
            },
            status=status.HTTP_200_OK
        )
