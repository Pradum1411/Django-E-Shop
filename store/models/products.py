from django.db import models
from .category import Category
class Product(models.Model):
    name=models.CharField(max_length=120)
    price=models.IntegerField(default=0)
    description=models.TextField(max_length=120,default="")
    image=models.ImageField(upload_to="upload/product_image", max_length=120)
    category=models.ForeignKey(Category, on_delete=models.CASCADE, default=1)

    # def __str__(self):
    #     return self.name