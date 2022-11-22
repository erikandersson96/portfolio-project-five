from django.db import models


class Product(models.Model):
    """
    Model for products
    """
    sku = models.CharField(max_length=254, null=True, blank=True)
    watch_make = models.CharField(max_length=254)
    watch_model = models.CharField(max_length=254)
    description = models.TextField()
    watch_size = models.DecimalField(max_digits=2, decimal_places=0)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.watch_model
