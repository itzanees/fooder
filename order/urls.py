from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),


     # authentication
    path('accounts/login/', views.loginview, name = "login"),
    path('accounts/signup/', views.signup, name = "signup"),
    path('logout', views.logout_view, name = 'logout'),
    path('reset',views.passwordreset, name='reset'),
]