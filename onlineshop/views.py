from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView


def show_home(request):
    return render(request, 'onlineshop/home.html')


def about(request):
    return render(request, 'onlineshop/community.html')


class PostListView(ListView):
    model = Post
    template_name = 'onlineshop/clothes.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post
    template_name = 'onlineshop/post_detail.html'
