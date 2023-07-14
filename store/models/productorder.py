from django.db import models
from .products import Product
from .customer import Customer

import datetime

class ProductOrder(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    price=models.IntegerField()
    address=models.TextField(max_length=50, default="", blank=True)
    mobile=models.IntegerField(blank=True)
    date=models.DateField(default=datetime.datetime.today)
    status=models.BooleanField(default=False)
    

    def placeorder(self):
        self.save()
  
    @staticmethod
    def get_orders_by_customer(customer_id):
        data=ProductOrder.objects.filter(customer=customer_id)
        return data    