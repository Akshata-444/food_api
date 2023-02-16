
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
     path('viewonly/', views.viewOnly),
     path('admin/<str:pk>', views.AdminSide),


]
