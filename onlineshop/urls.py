from django.urls import path
from . import views
from .views import PostListView, PostDetailView


urlpatterns = [
    path('', views.show_home, name='show_home'),
    path('community/', views.about, name='community'),
    path('clothes/', PostListView.as_view(), name='clothes'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    ]
