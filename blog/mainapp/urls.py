from django.urls import path

from .views import index, single


urlpatterns = [
    path('', index, name='main'),
    path('single/', single, name='single'),
]
