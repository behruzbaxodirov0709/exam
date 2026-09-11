from rest_framework import serializers
from . import models
from rest_framework.exceptions import ValidationError


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CategoryModel
        fields = "__all__"

    def validate_name(self, name):
        if name.isdigit():
            return ValidationError(detail="Kategoriya nomida harflar ham bo'lishi lozim")

        if len(name)<3:
            return ValidationError(detail="Kategoriya nomi kamida 4 ta harfdan iborat bo'lsin")

        return name


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductModel
        exclude = ["updated_at", "created_at"]


    def validate_name(self, name):
        if name.isdigit():
            return ValidationError(detail="Mahsulot nomida harflar ham bo'lishi lozim")

        if len(name)<3:
            return ValidationError(detail="Mahsulot nomi kamida 3 ta harfdan iborat bo'lsin")

        return name


    def validate_description(self, description):
        if description.isdigit():
            return ValidationError(detail="Mahsulot izohida harf ham bo'lishi lozim")

        if len(description)<30:
            return ValidationError(detail="Mahsulot izohi kamida 30 ta belgidan iborat jumla bo'lishi kerak")

        return description


    def validate_price(self, price):
        if price<=0:
            return ValidationError(detail="Mahsulot narxi noldan katta bo'lishi kerak")

        return price


