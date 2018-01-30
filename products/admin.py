from django.contrib import admin
from .models import Category, ProductImage, Products, Variation
# Register your models here.

admin.site.register(Products)
admin.site.register(Category)
admin.site.register(Variation)
admin.site.register(ProductImage)
