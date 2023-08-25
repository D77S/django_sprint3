from django.db.models import QuerySet
from django.http import HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.utils import timezone

from blog.models import Post, Category


def posts_selected() -> QuerySet:
    """Функция, ничего не принимает,
    возвращает модель (таблицу) Post
    с заджойненными к ней моделями (таблицами)
    Category, Location, User.
    Джойнимся по именам полей модели Post.
    Возвращаем вообще все поля, так как
    из всех вызовов функции есть хотя бы один,
    которому они нужны полностью все."""
    return Post.objects.select_related('category',
                                       'location',
                                       'author'
                                       )


def index(request) -> HttpResponse:
    """Функция для отображения главной страницы,
    принимает только стандартное заклинание request,
    возвращает отрендеренную страницу (главную).
    """
    posts = posts_selected().filter(is_published=True,
                                    category__is_published=True,
                                    pub_date__lte=timezone.now()
                                    ).order_by('-pub_date')[:5]
    context = {'post_list': posts, }
    return render(request, 'blog/index.html', context)


def post_detail(request, id: int) -> HttpResponse:
    """Функция для отображения всех данных
    по одному конкретному посту,
    принимает стандартное заклинание request и
    номер того поста, данные по которому надо отобразить,
    возвращает отрендеренную страницу (пост детально).
    """
    posts = posts_selected().filter(pk=id, is_published=True,
                                    category__is_published=True)
    post = get_object_or_404(posts, pub_date__lte=timezone.now())
    context = {'post': post}
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug: str) -> HttpResponse:
    """Функция для отображения всех постов одной из категорий,
    принимает стандартное заклинание request и
    слаг той категории, все посты которой надо отобразить,
    возвращает отрендеренную страницу (все посты заданной категории).
    """
    posts = posts_selected().filter(category__slug=category_slug,
                                    category__is_published=True,
                                    pub_date__lte=timezone.now()
                                    ).order_by('-pub_date')
    posts_or_404 = get_list_or_404(posts, is_published=True)
    # Мы точно знаем, что в модели Category
    # должнен быть объект (строка)
    # со слагом, равным переданному в функцию,
    # причем ровно один (уникальный).
    # Далее нам понадобятся некоторые его поля,
    # извлечем его весь для передачи в шаблон.
    selected_category_or_404 = get_object_or_404(Category.objects.all(),
                                                 slug=category_slug)
    context = {'post_list': posts_or_404, 'category': selected_category_or_404}
    return render(request, 'blog/category.html', context)
