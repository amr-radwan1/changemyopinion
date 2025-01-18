# opinions_app/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializers import PostSerializer

class PostListView(APIView):
    def get(self, request):
        posts = Post.objects.all()  # Retrieve all posts
        serializer = PostSerializer(posts, many=True)  # Serialize the posts
        return Response(serializer.data, status=status.HTTP_200_OK)
