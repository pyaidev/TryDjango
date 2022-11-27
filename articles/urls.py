from django.urls import path
from .views import (
    article_list_view,
    article_detail_view,
    article_search_view,
    article_create_view,
    article_update_view,
    article_delete_view,
)

app_name = 'articles'

urlpatterns = [
    path('', article_list_view, name='article_list'),
    path('detail/<slug:slug>/', article_detail_view, name='article_detail'),
    path('search/', article_search_view, name='article_search'),
    path('create/', article_create_view, name='article_create'),
    path('edit/<int:pk>/', article_update_view, name='article_update'),
    path('delete/<int:pk>/', article_delete_view, name='article_delete'),
]
