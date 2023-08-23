from django.http import HttpResponse
from django.shortcuts import get_list_or_404, render
from datetime import datetime

from blog.models import Post


def index(request) -> HttpResponse:
    posts = Post.objects.filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=datetime.now()
        ).order_by('-pub_date')[:5]
    context = {'post_list': posts, }
    return render(request, 'blog/index.html', context)


def post_detail(request, id: int) -> HttpResponse:
    context = {'post': posts[id]}
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug: str) -> HttpResponse:
    posts = get_list_or_404(
        Post.objects.select_related('category').filter(
            category__slug=category_slug,
            is_published=True,
            category__is_published=True,
            pub_date__lte=datetime.now()
            ).order_by('-pub_date'),
        is_published=True
        )
    context = {'post_list': posts}
    print(context)
    return render(request, 'blog/category.html', context)
