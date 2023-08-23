from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

from blog.models import Post


def index(request) -> HttpResponse:
    posts = Post.objects.filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=datetime.now()
        ).order_by('-pub_date')[:5]
    # Пока оставим тут лямбда-сортировку с прошлой версии проекта,
    # вдруг когда потом пригодится.
    # posts = sorted(posts, key=lambda x: x['id'], reverse=True)
    context = {'post_list': posts, }
    return render(request, 'blog/index.html', context)


def post_detail(request, id: int) -> HttpResponse:
    context = {'post': posts[id]}
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug: str) -> HttpResponse:
    context = {'temporary_slug': category_slug}
    return render(request, 'blog/category.html', context)
