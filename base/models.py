from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(null=True, max_length=127)
    description = models.TextField(null=True, max_length=2047)
    price = models.IntegerField(null=True, blank=True)
    rating = models.DecimalField(null=True, max_digits=2, decimal_places=1)
    isStock = models.BooleanField(null=True)
    quantity = models.IntegerField(null=True)
    created = models.DateTimeField(null=True, auto_now_add=True)
    updated = models.DateTimeField(null=True, auto_now=True)
    expiration = models.DateField(null=True)
    staticDiscount = models.IntegerField(null=True, default=0)
    percentageDiscount = models.IntegerField(null=True, default=0)
    # image = 




    def __str__(self):
        return self.title + ' ' + str(self.price)+ '$'

    pass



