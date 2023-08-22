from django.db import models
from django.contrib.auth import get_user_model

from core.models import PublishedCreatedModel, TitleModel

User = get_user_model()


class Category(PublishedCreatedModel, TitleModel):
    description = models.TextField(
        blank=False,
        default='Сначала пусто',
        verbose_name='Текст'
        )
    slug = models.SlugField(
        blank=False,
        default='Сначала пусто',
        verbose_name='Слаг',
        unique=True
        )

    class Meta:
        verbose_name = 'Тематическая категория'
        verbose_name_plural = 'Тематические категории'

    def __str__(self):
        return self.title


class Location(PublishedCreatedModel):
    name = models.CharField(
        blank=False,
        default='Сначала пусто',
        verbose_name='Имя локации',
        max_length=256
        )

    class Meta:
        verbose_name = 'Географическая метка'
        verbose_name_plural = 'Географические метки'

    def __str__(self):
        return self.name


class Post(PublishedCreatedModel, TitleModel):
    text = models.TextField(
        blank=False,
        default='Сначала пусто',
        verbose_name='Текст'
        )
    pub_date = models.DateTimeField(
        blank=False,
        auto_now_add=True,
        verbose_name='Когда, во-сколько опубликовано:'
        )
    author = models.ForeignKey(
        User,
        blank=False,
        null=True,
        default=None,
        on_delete=models.CASCADE,
        verbose_name='Автор'
        )
    location = models.ForeignKey(
        Location,
        blank=True,
        null=True,
        default=None,
        on_delete=models.SET_NULL,
        verbose_name='Локация'
        )
    category = models.ForeignKey(
        Category,
        blank=False,
        null=True,
        default=None,
        on_delete=models.SET_NULL,
        verbose_name='Категория'
        )

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return self.title
