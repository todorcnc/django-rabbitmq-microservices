from django.contrib import admin

from .models import Product, ProductUser

# Register your models here.
@admin.register(Product,ProductUser)
class AuthorAdmin(admin.ModelAdmin):
    pass