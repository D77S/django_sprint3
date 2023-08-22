# Generated by Django 3.2.16 on 2023-08-22 23:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_auto_20230822_2231'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Тематическая категория', 'verbose_name_plural': 'Тематические категории'},
        ),
        migrations.AlterModelOptions(
            name='location',
            options={'verbose_name': 'Географическая метка', 'verbose_name_plural': 'Географические метки'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Публикация', 'verbose_name_plural': 'Публикации'},
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='post',
            name='location',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.location', verbose_name='Локация'),
        ),
    ]