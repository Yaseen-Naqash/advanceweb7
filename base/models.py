from django.db import models
from django.contrib.auth.models import User


# class BaseModel(models.Model):
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
    


# Create your models here.
class Product(models.Model):
    title = models.CharField(null=True, max_length=127, verbose_name='عنوان')
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
    image = models.ImageField(upload_to='productsImages', null=True, blank=True)
    # pdf = models.FileField(upload_to='files', null=True)
    
    images = models.ManyToManyField('ProductImage')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'
        ordering = ['title', 'price']

    pass    

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    products = models.ManyToManyField(Product)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)



class Property(models.Model):
    title = models.CharField(max_length=127, null=True)
    value = models.CharField(max_length=127, null=True)
    products = models.ManyToManyField(Product)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    text = models.TextField(max_length=2047, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)

class ProductImage(models.Model):
    image = models.ImageField(upload_to='productsImages', null=True)
    # product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)