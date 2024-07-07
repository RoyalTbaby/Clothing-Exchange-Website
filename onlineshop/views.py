from time import timezone
from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def show_home(request):
    return render(request, 'onlineshop/home.html')


def about(request):
    return render(request, 'onlineshop/community.html')


def clothes(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'onlineshop/clothes.html', context)
