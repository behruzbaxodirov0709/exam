from django.db import models


class CategoryModel(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name






class ProductModel(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    category = models.ForeignKey(to=CategoryModel, on_delete=models.PROTECT)
    image = models.ImageField(upload_to="media/", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    count = models.PositiveIntegerField(default=1)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name if len(self.name) <= 30 else f"{self.name[0:30]} ..."

    