from django import template

from mainapp.models import Post, Tag


register = template.Library()


@register.inclusion_tag('mainapp/popular_posts_tpl.html')
def get_popular(cnt=3):
    """
    Выводит наиболее просматриваемые посты (по умолчанию - 3)
    """
    posts = Post.objects.order_by('-views')[:cnt]
    return {'posts': posts}


@register.inclusion_tag('mainapp/tags_tpl.html')
def get_tags():
    """Выводит облако тегов"""
    tags = Tag.objects.all()
    return {'tags': tags}
