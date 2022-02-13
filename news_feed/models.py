from django.conf import settings
from django.db import models


class Post(models.Model):

    title = models.CharField(
        max_length=120,
        verbose_name='Заголовок статьи',
    )
    # todo Change character limit
    content = models.CharField(
        max_length=100000,
        verbose_name='Текст статьи',
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        verbose_name='Автор',
    )
    created_on = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата и время создания',
    )
    updated_on = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата и время последнего изменения',
    )
    # Не публичные статьи могут видеть только авторизованные пользователи
    is_public = models.BooleanField(
        default=True,
        verbose_name='Публичная статья',
    )


