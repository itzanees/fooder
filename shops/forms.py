from django.forms import ModelForm

from menus.models import Dish

class DishesForm(ModelForm):
    class Meta:
        model = Dish
        fields = ['category', 'image', 'title', 'description', 'price' ]