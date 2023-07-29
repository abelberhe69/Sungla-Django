from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='index'),
    path('about/', views.about, name='about'),
    path('glasses/', views.glasses, name='glasses'),
    path('shop/', views.shop, name='shop'),
    path('contact/', views.contact, name='contact')
]