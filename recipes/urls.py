from django.urls import path
from .views import (
    recipe_list_view,
    recipe_detail_view,
    recipe_create_view,
    recipe_edit_view,
    recipe_delete_view,
)

app_name = 'recipes'

urlpatterns = [
    path('list/', recipe_list_view, name='list'),
    path('detail/<slug:slug>/', recipe_detail_view, name='detail'),
    path('create/', recipe_create_view, name='create'),
    path('edit/<int:pk>/', recipe_edit_view, name='edit'),
    path('delete/<int:pk>/', recipe_delete_view, name='delete'),

]
