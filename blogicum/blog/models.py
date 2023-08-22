from asyncio.windows_events import NULL
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


class Location(PublishedCreatedModel):
    name = models.CharField(
        blank=False,
        default='Сначала пусто',
        verbose_name='Имя локации',
        max_length=256
        )


class Post(PublishedCreatedModel, TitleModel):
    text = models.TextField(
        blank=False,
        default='Сначала пусто',
        verbose_name='Текст'
        )
    pub_date = models.DateTimeField(
        blank=False,
        verbose_name='Когда, во-сколько опубликовано:'
        )
    author = models.ForeignKey(
        User,
        blank=False,
        null=True,
        default=NULL,
        on_delete=models.CASCADE,
        verbose_name='Автор'
        )
    location = models.ForeignKey(
        Location,
        blank=True,
        null=True,
        default=NULL,
        on_delete=models.SET_NULL,
        verbose_name='Локация'
        )
    category = models.ForeignKey(
        Category,
        blank=False,
        null=True,
        default=NULL,
        on_delete=models.SET_NULL,
        verbose_name='Категория'
        )

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
        ordering = ('title',)

    def __str__(self):
        return self.title
