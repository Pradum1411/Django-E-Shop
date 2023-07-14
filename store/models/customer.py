from django.db import models

class Customer(models.Model):
    name=models.CharField(max_length=120)
    mobile=models.IntegerField(default=0)
    email=models.EmailField(max_length=120)
    password=models.TextField(max_length=100)

    # def __str__(self):
    #     return self.name
    #  jab foreignkey use karenge to name dikhega id nhi