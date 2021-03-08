from django.db import models

# Create your models here

class pincode(models.Model):
    pincode = models.IntegerField()
    city = models.CharField(max_length=200)


