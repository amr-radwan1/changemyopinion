# opinions_app/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializers import PostSerializer
from .models import User
from .serializers import UserSerializer
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

class PostListView(APIView):
    def get(self, request):
        posts = Post.objects.all()  # Retrieve all posts
        serializer = PostSerializer(posts, many=True)  # Serialize the posts
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        # Deserialize the incoming data
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the data as a new Post object
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginUserView(APIView):
    def post(self, request):
        username = request.data.get('Username')
        if username:
            user = User.objects.filter(Username=username).first()
        if not user:
            return Response({"error": "User not found."}, status=status.HTTP_400_BAD_REQUEST)
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

def logout_user(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout
