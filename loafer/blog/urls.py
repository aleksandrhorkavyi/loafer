from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='blog_index'),
    path('tags/', tags, name='tags_url'),
    path('tags/create/', TagCreate.as_view(), name='tag_create_url'),
    path('tags/update/<str:slug>/', TagUpdate.as_view(), name='tag_update_url'),
    path('tags/delete/<str:slug>/', TagDelete.as_view(), name='tag_delete_url'),
    path('create/', PostCreate.as_view(), name='post_create_url'),
    path('update/<str:slug>/', PostUpdate.as_view(), name='post_update_url'),
    path('delete/<str:slug>/', PostDelete.as_view(), name='post_delete_url'),
    path('<str:slug>/', PostView.as_view(), name='view_url'),
    path('tags/<str:slug>/', TagView.as_view(), name='tags_view_url'),
]
