from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Brand(models.Model):
    brand_name = models.CharField(max_length=100)
    brand_founded = models.DateField(default=timezone.now)
    brand_logo = models.ImageField(upload_to='cars/media/brandLogo/', blank=True, null=True)
    brand_slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    def __str__(self):
        return self.brand_name

class Car(models.Model):
    car_name = models.CharField(max_length=100)
    car_image = models.ImageField(upload_to='cars/media/carPicture/', blank=True, null=True)
    car_price = models.IntegerField()
    car_quantity = models.IntegerField()
    car_description = models.TextField(max_length=400)
    car_brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='cars')

    def __str__(self):
        return self.car_name

class CarComments(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    comment_author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_on = models.DateField(auto_now_add=True)

    def __repr__(self):
        return self.car.car_name