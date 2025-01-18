# opinions_app/urls.py
from django.urls import path
from .views import PostListView
from .views import login_user

urlpatterns = [
    path('posts/', PostListView.as_view(), name='post-list'),  # API endpoint for getting all posts
    path('login/', login_user, name='login'),  # Use the function-based view directly
]