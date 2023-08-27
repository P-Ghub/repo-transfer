from django.db import models

# Logos Class
class storeItem(models.Model):
    image = models.ImageField(upload_to='images/')
    info = models.CharField(max_length=200)
    brand = models.CharField(max_length=200, default='brand')

    def __str__(self):
        return self.info
    
# Stock Class
class stockItem(models.Model):
    image = models.ImageField(upload_to='images/')
    info = models.CharField(max_length=200)
    brand = models.CharField(max_length=200, default='brand')
    price = models.CharField(max_length=200, default='price')

    def __str__(self):
        return self.info
    
