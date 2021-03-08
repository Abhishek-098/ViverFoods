from django.db import models

# Create your models here.

class product(models.Model):

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'pics')
    price = models.FloatField()
    offer = models.BooleanField(default=False)
    category = models.CharField(max_length=100)
    offer_price = models.FloatField( default=0)
    price_before = models.FloatField( default=0)






