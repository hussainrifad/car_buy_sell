from django.shortcuts import render
from cars.models import Car, Brand

def home(request, brand_slug=None):
    cars = Car.objects.all()
    if brand_slug is not None:
        brand = Brand.objects.get(brand_slug=brand_slug)
        cars = Car.objects.filter(car_brand = brand)
    brands = Brand.objects.all()
    return render(request, 'home.html', {'brands':brands, 'cars':cars})