from django.shortcuts import render, redirect
from cars.models import Car
from cart.models import UserCart
# Create your views here.

def add_to_cart(request,id):
    car = Car.objects.get(id=id)
    # reducing the car quantity in the database 
    car.car_quantity -= 1
    car.save()

    cart_item, created = UserCart.objects.get_or_create(buyer=request.user, car=car)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('profile')