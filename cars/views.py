from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView
from .models import Car, Brand, CarComments
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import CarForm, BrandForm, CarCommentForm
from datetime import date

# Create your views here.

class CarAddCreateView(CreateView):
    model = Car
    template_name = 'addCar.html'
    success_url = reverse_lazy('home')
    form_class = CarForm

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect('userlogin')
    
    def form_valid(self, form):
        messages.success(self.request, 'Car Added Successfully')
        return super().form_valid(form=form)
    
    def form_invalid(self, form):
        return super().form_valid(form=form)

class BrandAddCreateView(CreateView):
    model = Brand
    template_name = 'addBrand.html'
    success_url = reverse_lazy('home')
    form_class = BrandForm

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect('userlogin')
    
    def form_valid(self, form):
        messages.success(self.request, 'Brand Added Successfully')
        return super().form_valid(form=form)
    
    def form_invalid(self, form):
        return super().form_valid(form=form)

class CarDetailView(DetailView):
    model = Car
    pk_url_kwarg = 'id'
    template_name = 'carDetails.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['car'] = self.get_object()
        return context

def createComment(request, id):
    car = Car.objects.get(id=id)
    comments = CarComments.objects.filter(car=car)
    
    if request.method == 'POST':
        form = CarCommentForm(request.POST)
        if form.is_valid():
            comment = form.cleaned_data['comment']
            s_comment, created = CarComments.objects.get_or_create(car=car, comment_author=request.user, comment=comment)
            s_comment.save()
            messages.success(request, 'Comments added')
            return redirect('home')
    else:
        form = CarCommentForm()
    return render(request, 'comments.html', {'form':form, 'comments':comments, 'today':date.today()})