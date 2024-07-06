from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_home, name='show_home'),
    path('clothes/', views.clothes, name='clothes'),
    path('community/', views.about, name='community'),
]