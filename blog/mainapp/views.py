from django.shortcuts import render
from django.views.generic import ListView, DetailView

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
    paginate_by = 1
    allow_empty = False

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs['slug'])
        return context


def get_post(request, slug):
    return render(request, 'mainapp/category.html')


def get_category(request, slug):
    return render(request, 'mainapp/category.html')
