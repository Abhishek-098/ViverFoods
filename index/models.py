from django.db import models
from django.contrib.auth.models import User
from breakfast.models import product
import datetime

# Create your models here.
class status(models.Model):
    status = models.CharField(max_length=30)

class orders(models.Model):
    product = models.ForeignKey(product,on_delete=models.CASCADE)
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    date = models.DateField(default=datetime.datetime.today)
    landmark = models.CharField(max_length=200,default='jaypee university')
    city = models.CharField(max_length=100,default='Guna')
    pincode = models.IntegerField(default=473226)
    phone = models.CharField(max_length=10,default=1234567890)
    orderStatus = models.ForeignKey(status,on_delete=models.CASCADE,default=1)

def placeorder(self):
    self.save()