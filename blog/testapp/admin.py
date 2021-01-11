from django.contrib import admin

from .models import Rubric
from mptt.admin import MPTTModelAdmin


class CustomMPTTModelAdmin(MPTTModelAdmin):
    """Кастомный класс вывода данных в админки"""
    mptt_level_indent = 20


admin.site.register(Rubric, CustomMPTTModelAdmin)
