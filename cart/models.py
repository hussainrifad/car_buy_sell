from django.db import models
from django.contrib.auth.models import User
from cars.models import Car
# Create your models here.

class UserCart(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.buyer.first_name