from enum import unique
from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.IntegerField(primary_key=True,auto_created=False, unique=True,editable=True)
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
     

class ProductUser(models.Model):
    user_id = models.IntegerField(unique=True)
    product_id = models.IntegerField()