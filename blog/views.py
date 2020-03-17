from django.shortcuts import render

posts = [
    {
        'author': 'Tienanh',
        'title': 'blog post 1',
        'content': "first post content",
        'date_posted': 'august 27,2018'
    },
    {
        'author': 'Jack',
        'title': 'blog post 2',
        'content': "second post content",
        'date_posted': 'august 28,2018'
    }

]


def showHome(req):
    context = {
        'posts': posts,
        'title': "mytitle"
    }
    return render(req, 'blog/home.html', context)


def about(req):
    return render(req, 'blog/about.html', {'title': 'about'})
