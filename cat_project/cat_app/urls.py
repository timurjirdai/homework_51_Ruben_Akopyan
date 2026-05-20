from django.urls import path
from .views import index, cat_view

urlpatterns = [
    path('', index, name='index'),
    path('cat/', cat_view, name='cat'),
]