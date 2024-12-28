from django.urls import path
from . import views

urlpatterns = [
    path('become-seller/', views.become_seller, name='become_seller'),
    path('sell/', views.sell, name="sell"),
    path('add_dish/', views.add_dish, name='add_dish'),

]