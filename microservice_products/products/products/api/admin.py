from django.contrib import admin

from .models import Product, User

# Register your models here.
@admin.register(Product,User)
class AuthorAdmin(admin.ModelAdmin):
    pass