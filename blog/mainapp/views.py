# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import F

from .models import Tag, Post, Category


class Home(ListView):
    """Вывод главной страницы"""
    model = Post
    template_name = 'mainapp/index.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Classic Blog Design'
        return context


class PostsByCategory(ListView):
    """Вывод статей по категориям"""
    model = Post
    template_name = 'mainapp/index.html'
    context_object_name = 'posts'
    paginate_by = 4
    allow_empty = False

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs['slug'])
        return context


class PostsByTag(ListView):
    """Выводит тэги"""
    template_name = 'mainapp/index.html'
    context_object_name = 'posts'
    paginate_by = 1
    allow_empty = False

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Записи по тегу: ' + str(Tag.objects.get(slug=self.kwargs['slug']))
        return context


class GetPost(DetailView):
    """Показывает каждый пост отдельно"""
    model = Post
    template_name = 'mainapp/single.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # выражение, которое увеличивает кол-во просмотров
        self.object.views = F('views') + 1
        self.object.save()  # сохраняем объект
        self.object.refresh_from_db()   # перезапрашивает данный из бд
        return context


class Search(ListView):
    """Поиск данных по сайту"""
    template_name = 'mainapp/search.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_queryset(self):
        return Post.objects.filter(title__icontains=self.request.GET.get('s'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # пагинация для поиска(шаблона search) - добавляем
        # переменную s в контекст
        context['s'] = f"s={self.request.GET.get('s')}&"
        return context
