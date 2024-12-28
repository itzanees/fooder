from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify

from .models import Shop
from menus.models import Dish

from .forms import DishesForm

# Create your views here.

def become_seller(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            shop = Shop.objects.create(name = user.username, created_by = user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'sellers/become_seller.html', {'form':form})

@login_required
def sell(request):
    shops = request.user.shop
    dishes = shops.dishes.all()
    return render(request, 'sellers/sell.html', {'seller':shops,'dishes':dishes})


@login_required
def add_dish(request):
    if request.method == 'POST':
        form = DishesForm(request.POST, request.FILES)
        if form.is_valid():
            dish = form.save(commit=False)
            dish.shop = request.user.shop
            dish.slug = slugify(dish.title)
            dish.save()

            return redirect('sell')
    else:
        form = DishesForm()
    
    return render (request, 'sellers/add_dish.html', {'form':form})
