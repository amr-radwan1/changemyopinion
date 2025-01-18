# opinions_app/urls.py
from django.urls import path
from .views import PostListView
from .views import login_user

urlpatterns = [
    path('posts/', PostListView.as_view(), name='post-list'),  # API endpoint for getting all posts
]

urlpatterns = [
    path('login/', login_user.as_view(template_name='users/login.html'), name='login'),
]