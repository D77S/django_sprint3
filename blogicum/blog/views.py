from django.http import HttpResponse
from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.utils import timezone
from datetime import datetime

from blog.models import Post, Category


def index(request) -> HttpResponse:
    posts = Post.objects.filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=datetime.now(tz=timezone.utc)
        ).order_by('-pub_date')[:5]
    context = {'post_list': posts, }
    return render(request, 'blog/index.html', context)


def post_detail(request, id: int) -> HttpResponse:
    post1 = Post.objects.select_related(
        'category').filter(pk=id, is_published=True,
                           category__is_published=True)
    post = get_object_or_404(
        post1, pub_date__lte=datetime.now(tz=timezone.utc))
    context = {'post': post}
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug: str) -> HttpResponse:
    posts1 = Post.objects.select_related('category').filter(
            category__slug=category_slug,
            category__is_published=True,
            pub_date__lte=datetime.now(tz=timezone.utc)
            ).order_by('-pub_date')
    cat1 = Category.objects.get(slug=category_slug)
    posts = get_list_or_404(posts1, is_published=True)
    context = {'post_list': posts, 'category': cat1}
    return render(request, 'blog/category.html', context)
