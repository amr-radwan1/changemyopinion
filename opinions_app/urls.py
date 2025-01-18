# opinions_app/urls.py
from django.urls import path
from .views import UserListView, PostListView, FollowerListView, PromptListView, LogoutUserView, UpdateVotesView, RegisterUserView

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('posts/', PostListView.as_view(), name='post-list'),
    path('users/<int:userid>/followers/', FollowerListView.as_view(), name='follower-list'),
    path('prompts/', PromptListView.as_view(), name='prompt-list'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('posts/<int:post_id>/<str:vote_type>/', UpdateVotesView.as_view(), name='update-votes'),
    path('register/', RegisterUserView.as_view(), name='register')
]
