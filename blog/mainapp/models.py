from django.db import models
from django.urls import reverse


class Category(models.Model):

    title = models.CharField('Категория', max_length=255)
    slug = models.SlugField('Url' ,max_length=255, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']


class Tag(models.Model):

    title = models.CharField('Тег', max_length=50)
    slug = models.SlugField('Url', max_length=50, unique=True)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tag', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['title']


class Post(models.Model):

    title = models.CharField('Название поста', max_length=255)
    slug = models.SlugField('Url', max_length=255, unique=True)
    author = models.CharField('Автор', max_length=100)
    content = models.TextField('Контент', blank=True)
    created_at = models.DateTimeField(
        'Опубликовано',
        auto_now_add=True
    )
    photo = models.ImageField('Изображение', upload_to='photos/%Y/%m/%d/', blank=True)
    views = models.IntegerField('Колличество просмотров', default=0)
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='posts',
        verbose_name='Категория'
    )
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        related_name='posts',
        verbose_name='Теги'
    )
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-created_at']
