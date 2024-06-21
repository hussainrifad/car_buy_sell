from . import views
from django.urls import path

urlpatterns = [
    path('registration/', views.UserCreateView.as_view(), name='registration'),
    path('login/', views.UserLoginView.as_view(), name='userlogin'),
    path('logout/', views.UserLogoutView.as_view(), name='userlogout'),
    path('updateprofile/', views.UserUpdateView.as_view(), name='updateprofile'),
    path('profile/', views.profile, name='profile'),
]