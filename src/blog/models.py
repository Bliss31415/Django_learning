from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

from django_learn import settings

class Post(models.Model):
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        verbose_name='Автор',
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