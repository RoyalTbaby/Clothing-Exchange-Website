from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_home, name='show_home'),
    path('about/', views.about, name='about'),
]