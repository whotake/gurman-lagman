from django.db import models


class Category(models.Model):
    parent = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        verbose_name='Родительская категория',
        blank=True,
        null=True
    )
    name = models.CharField(
        verbose_name='Название',
        max_length=60
    )
    description = models.CharField(
        verbose_name='Описание',
        max_length=250
    )

    def __str__(self):
        return self.name


class Place(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=60
    )
    description = models.TextField(
        max_length=5000,
        verbose_name='Описание'
    )
    category = models.ManyToManyField(
        Category,
        verbose_name='Категории'
    )

    def __str__(self):
        return self.name
