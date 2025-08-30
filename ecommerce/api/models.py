# from django.db import models

# # Create your models here.
# class Product(models.Model):
#     name = models.TextField(blank=True, null=True)
#     description = models.CharField(max_length=100)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     category = models.CharField(max_length=100)
#     stock_Quantity = models.IntegerField()
#     image_url = models.URLField(blank=True, null=True)
#     created_Date = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.name
    
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products', null=True, blank=True) #New Filds for authenticated users.
    name = models.TextField(blank=True, null=True)
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    stock_quantity = models.IntegerField(default=0)
    image_url = models.URLField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    # created_date = models.DateTimeField(auto_now_add=True, default=timezone.now)
    

    def __str__(self):
        return self.name




