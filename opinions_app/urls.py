# opinions_app/urls.py
from django.urls import path
from .views import PostListView

urlpatterns = [
    path('posts/', PostListView.as_view(), name='post-list'),  # API endpoint for getting all posts
]
