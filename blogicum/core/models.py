from django.db import models


class PublishedCreatedModel(models.Model):
    is_published = models.BooleanField(
        blank=False,
        default=True,
        verbose_name='Опубликовано',
        help_text='Снимите галочку, чтобы скрыть публикацию.'
        )
    created_at = models.DateTimeField(
        blank=False,
        auto_now_add=True,
        verbose_name='Добавлено'
        )

    class Meta:
        abstract = True


class TitleModel(models.Model):
    title = models.CharField(
        blank=False,
        max_length=256,
        default='Сначала пусто',
        verbose_name='Заголовок',
        null=True
        )

    class Meta:
        abstract = True
