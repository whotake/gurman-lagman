from django.db import models

from place.models import Place


class Article(models.Model):
    title = models.CharField(
        verbose_name='Заголовок',
        max_length=100
    )
    body = models.TextField(
        verbose_name='Текст'
    )
    place = models.ForeignKey(
        Place,
        on_delete=models.SET_NULL,
        verbose_name='Место',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title[:50]
