from django.db import models
from django.urls import reverse

from mptt.models import MPTTModel, TreeForeignKey



class Rubric(MPTTModel):
    """Рубрика"""
    name = models.CharField('Имя', max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE,
                            null=True, blank=True,
                            related_name='children',
                            verbose_name='Родитель')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('rubric', kwargs={'pk': self.pk})

    class MPTTMeta:
        order_insertion_by = ['name']


class Article(models.Model):

    name = models.CharField('Имя', max_length=250)
    category = TreeForeignKey(Rubric, on_delete=models.PROTECT,
                              verbose_name='Категория')

    def __str__(self):
        return self.name
