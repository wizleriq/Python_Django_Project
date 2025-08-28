from django.db import models

# Create your models here.
class Produt(models.Model):
    name = models.TextField(blank=True, null=True)
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    stock_Quantity = models.IntegerField()
    image_url = models.URLField(blank=True, null=True)
    created_Date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

