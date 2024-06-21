from django.contrib import admin
from .models import Car, Brand, CarComments
# Register your models here.

class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {'brand_slug' : ('brand_name',)}
    list_display = ['brand_name', 'brand_slug']

admin.site.register(Car)
admin.site.register(Brand, BrandAdmin)
admin.site.register(CarComments)