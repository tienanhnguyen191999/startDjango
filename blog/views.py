from django.shortcuts import render
from .models import Post

# controller File


def showHome(req):
    context = {
        'posts': Post.objects.all(),
        'title': "mytitle"
    }
    return render(req, 'blog/home.html', context)


def about(req):
    return render(req, 'blog/about.html', {'title': 'about'})
