from django.contrib import admin
from .models import FoodData, FoodItem
# Register your models here.
admin.site.register(FoodData)
admin.site.register(FoodItem)