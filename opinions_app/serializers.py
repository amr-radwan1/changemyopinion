# opinions_app/serializers.py
from rest_framework import serializers
from .models import Post
from .models import User


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['PostID', 'UserID', 'UpvoteCount', 'DownvoteCount', 'CreatedAt', 'PostText']
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'UserID',
            'Username',
            'Email',
            'ProfilePicture',
            'JoinDate',
            'Bio',
            'ReplyPoints',
            'Followers',  # Followers is an ArrayField
        ]
