from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Shop(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.OneToOneField(User, related_name = 'shop', on_delete=models.CASCADE)

    class Meta():
        ordering = ['name']

    def __str__(self):
        return self.name