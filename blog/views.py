from blog.data import posts
from django.shortcuts import render

from . import data


def blog(request):
    print('blog')

    context = {
        #'text': 'Estamos no blog',
        'posts': posts
    }

    return render(
        request,
        'blog/index.html',
        context,
    )

def post(request, id):
    print('post', id)

    context = {
        #'text': 'Estamos no blog',
        'posts': posts
    }

    return render(
        request,
        'blog/index.html',
        context,
    )


def exemplo(request):
    print('exemplo')

    context = {
        'text': 'Estamos no exemplo'
    }

    return render(
        request,
        'blog/exemplo.html',
        context,

    )