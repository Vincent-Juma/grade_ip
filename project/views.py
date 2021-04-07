from django.shortcuts import render
from __future__ import unicode_literals
from .models import Post


def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'project/home.html', context)

def about(request):
    return render(request, 'project/about.html', {'title': 'About'})

def info(request):
    return render(request, 'project/info.html', {'title': 'Info'})

