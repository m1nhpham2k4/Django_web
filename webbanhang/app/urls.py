from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('card/', views.card, name="card"),
    path('checkout/', views.checkout, name="checkout"),
]