from django.shortcuts import render


posts = [
    {
        'author': 'Dereck',
        'title': 'Post #1',
        'content': 'first post',
        'date_posted': 'May 8th, 2022'
    },
    {
        'author': 'Dereck',
        'title': 'Post #2',
        'content': 'second post',
        'date_posted': 'May 20th, 2022'
    }
]


def home(request):
    context = {
        'posts': posts
    }

    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
