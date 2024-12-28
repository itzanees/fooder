import random

from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from .models import Category, Dish

def  dish(request, category_slug, dish_slug):
    dish = get_object_or_404(Dish, category__slug =category_slug, slug = dish_slug)
    similar_dishes = list(dish.category.dishes.exclude(id=dish.id))

    if len(similar_dishes)>=4:
        similar_dishes = random.sample(similar_dishes, 4)

    return render (request, 'menu/menu.html', {'dish':dish, 'similar_dishes':similar_dishes} )


def category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)

    return render (request, 'menu/category.html', {'category':category} )

def search(request):
    query = request.GET.get('query', '')
    dishes = Dish.objects.filter(Q(title__icontains = query) | Q(description__icontains = query))

    return render(request, 'menu/search.html', {'dishes':dishes, 'query':query})