from django.urls import path

from . import views

urlpatterns = [
    path('<slug:category_slug>/<slug:dish_slug>/', views.dish, name='dish'),
    path('<slug:category_slug>', views.category, name='category'),
    path('search/', views.search, name='search'),
]