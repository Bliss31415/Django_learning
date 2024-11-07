from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.CharField(
        verbose_name='Автор',
        max_length=255,
    )

    title = models.CharField(
        verbose_name='Заголовок',
        max_length=255,
    )

    text = models.TextField(
        verbose_name='Текст поста',
    )

    create_at = models.DateTimeField(
        verbose_name='Дата создания',
        default=timezone.now
    )

    def __str__(self):
        return self.title