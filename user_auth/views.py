from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib import messages
from . import forms
from cart.models import UserCart
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


# Create your views here.

class UserCreateView(CreateView):
    model = User
    form_class = forms.UserRegistrationForm
    template_name = 'register.html'
    success_url = reverse_lazy('userlogin')

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('profile')
        else:
            return super().dispatch(request, *args, **kwargs)
            
    def form_valid(self, form):
        messages.success(self.request, 'User Created Successfully')
        return super().form_valid(form=form)
    
    def form_invalid(self, form):
        return super().form_invalid(form=form)

class UserLoginView(LoginView):
    template_name = 'login.html'

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('profile')
        else:
            return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request, 'User Logged in Successfully')
        return super().form_valid(form=form)
    
    def form_invalid(self, form):
        return super().form_invalid(form=form)

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('home')


class UserUpdateView(UpdateView):
    form_class = forms.UpdateProfileForm
    success_url = reverse_lazy('profile')
    template_name = 'editProfile.html'

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect('userlogin')      
    
    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, 'User updated successfully')
        return super().form_valid(form=form)
    
    def form_invalid(self, form):
        messages.warning(self.request, 'Invalid User Data')
        return super().form_invalid(form=form)

def profile(request):
    if request.user.is_authenticated:
        items = UserCart.objects.filter(buyer=request.user)
        if items:
            for item in items:
                print(item.car.car_name)
        return render(request, 'profile.html', {'items':items})
    else:
        return redirect('userlogin')