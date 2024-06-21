from .models import Brand, Car, CarComments
from django.forms import ModelForm
from django import forms

class BrandForm(ModelForm):
    class Meta:
        model = Brand
        fields = ['brand_name', 'brand_logo', 'brand_founded']

        widgets = {
            'brand_name' : forms.TextInput(attrs={'id':'required'}),
            'brand_founded' : forms.DateInput(attrs={'type':'date'})
        }
        # labels = {

        # }
        # help_texts = {

        # }

class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

        widgets = {
            'car_name' : forms.TextInput(attrs={'id':'required'}),
            'car_description' : forms.Textarea(attrs={'rows':5})
        }

class CarCommentForm(ModelForm):
    class Meta:
        model = CarComments
        fields = ['comment']

        widgets = {
            'comment' : forms.Textarea(attrs={'rows':5}),
        }