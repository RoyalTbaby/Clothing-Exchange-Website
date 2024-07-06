from time import timezone
from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponse

posts = [{
    'author': 'Julianna Daffner',
    'title': 'Post 1',
    'content': 'welcome to my blog',
    'date': timezone.now()
},

    {
        'author': 'Jane Doe',
        'title': 'Post 3',
        'content': 'i am dead',
        'date': '2nd October, 3933',
    }
]


def show_home(request):
    return render(request, 'onlineshop/home.html')


def about(request):
    return render(request, 'onlineshop/community.html')


def clothes(request):
    context = {
        'posts': posts
    }
    return render(request, 'onlineshop/clothes.html', {'posts': posts})
