from asyncio.windows_events import NULL
from datetime import datetime
from django.db import models
# from core.models import PublishedCreatedModel, TitleModel
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
#  class Post(PublishedCreatedModel, TitleModel):
    title = models.CharField(
        blank=False,  # Знаю, что оно так по дефолту.
                      # Пока учусь - лишний раз пропишу.
        max_length=256,
        default='Сначала пусто',
        verbose_name='Название',
        on_delete=models.SET_NULL,
        null=True
        )
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
        defaul=NULL,
        on_delete=models.CASCADE,
        verbose_name='Автор'
        )
    location = models.ForeignKey(
        Location,
        blank=True,
        null=True,
        defaul=NULL,
        on_delete=models.SET_NULL,
        verbose_name='Локация'
        )
    category = models.ForeignKey(
        Category,
        blank=False,
        null=True,
        defaul=NULL,
        on_delete=models.SET_NULL,
        verbose_name='Категория'
        )
    is_published = models.BooleanField(
        blank=False,
        default=True,
        verbose_name='Опубликовано',
        )
    created_at = models.DateTimeField(
        blank=False,
        default=datetime.now,
        verbose_name='Когда, во-сколько создано:'
        )

    # description = models.TextField(verbose_name='Описание')
    # wrapper = models.OneToOneField(
    #     Wrapper,
    #     on_delete=models.SET_NULL,
    #     related_name='ice_cream',
    #     null=True,
    #     blank=True,
    #     verbose_name='Обёртка'
    # )
    # category = models.ForeignKey(
    #     Category,
    #     on_delete=models.CASCADE,
    #     related_name='ice_creams',
    #     verbose_name='Категория'
    # )
    # toppings = models.ManyToManyField(
    #    Topping,
    #     verbose_name='Топпинги'
    #     )
    # is_on_main = models.BooleanField(
    #     default=False,
    #     verbose_name='На главную',
    #     )
    # output_order = models.PositiveSmallIntegerField(
    #     default=100,
    #     verbose_name='Порядок отображения'
    # )
    # price = models.DecimalField(
    #     decimal_places=2,
    #     max_digits=4,
    #     verbose_name='Цена',
    # )

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
        ordering = ('title')

    def __str__(self):
        return self.title







# class Category(PublishedCreatedModel, TitleModel):
#    description = models.TextField()
#    slug = models.SlugField(unique=True)


# class Location(PublishedCreatedModel):
#    name = models.CharField(max_length=256)
