from django.db import models
from django.db.models.signals import post_save
from django.urls import reverse

# Create your models here

class Products(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    active = models.BooleanField(default=True)
    categories = models.ManyToManyField('Category', blank=True)
    default = models.ForeignKey('Category',related_name='default_category',null=True,blank=True, on_delete =models.DO_NOTHING)


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse("product_detail",kwargs={"pk":self.pk})


class ProductImage(models.Model):
    product = models.ForeignKey(Products, on_delete =models.DO_NOTHING)
    image = models.ImageField(upload_to='products/')



    def __str__(self):
        return self.product.title




class Category(models.Model):
    title = models.CharField(max_length=256)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title



class Variation(models.Model):
    product = models.ForeignKey(Products, on_delete =models.DO_NOTHING)
    title = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    sale_price = models.DecimalField(null=True, blank=True, max_digits=20, decimal_places=2)
    active = models.BooleanField(default=True)
    inventory = models.IntegerField(null=True,blank=True)


    def __str__(self):
        return self.title


def product_post_saved_receiver(sender, instance, *args, **kwargs):
    product = instance
    variation = product.variation_set.all()
    if variation.count() == 0:
        new_variation = Variation()
        new_variation.product = product
        new_variation.price = product.price
        new_variation.title = "Default"
        new_variation.save()



post_save.connect(product_post_saved_receiver, sender=Products)
