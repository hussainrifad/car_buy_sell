from django.urls import path
from . import views

urlpatterns = [
    path('add_brand/', views.BrandAddCreateView.as_view(), name='addbrand'),
    path('add_car/', views.CarAddCreateView.as_view(), name='addcar'),
    path('car_details/<int:id>', views.CarDetailView.as_view(), name='car_details'),
    path('all_comments/<int:id>', views.createComment, name='comments')
]