from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MenuItem(models.Model):
    TYPES = [
        ('0', 'تخصصی'),
        ('1', 'تجاری'),

        
    ]
    title = models.CharField(max_length=127, null=True)
    ingerdiants = models.TextField(max_length=2047, null=True)
    price = models.IntegerField(null=True)
    type = models.CharField(max_length=1, null=True, choices=TYPES)

    def __str__(self):
        return self.title

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  
    menuItem = models.ManyToManyField(MenuItem)



