from django.db import models
from datetime import datetime


class PublishedCreatedModel(models.Model):
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

    class Meta:
        abstract = True


class TitleModel(models.Model):
    title = models.CharField(
        blank=False,
        max_length=256,
        default='Сначала пусто',
        verbose_name='Название',
        null=True
        )

    class Meta:
        abstract = True
