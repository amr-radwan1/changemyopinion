# opinions_app/urls.py
from django.urls import path
from .views import UserListView, PostListView, FollowerListView, PromptListView, LogoutUserView

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('posts/', PostListView.as_view(), name='post-list'),
    path('users/<int:userid>/followers/', FollowerListView.as_view(), name='follower-list'),
    path('prompts/', PromptListView.as_view(), name='prompt-list'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
]
