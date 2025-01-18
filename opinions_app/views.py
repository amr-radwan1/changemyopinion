from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User, Post, Prompt, Reply
from .serializers import UserSerializer, PostSerializer, PromptSerializer
from django.shortcuts import redirect
from django.contrib.auth import logout


class UserListView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostListView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FollowerListView(APIView):
    def get(self, request, userid):
        try:
            user = User.objects.get(pk=userid)
            followers = user.Followers or []
            return Response({"followers": followers}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, userid):
        try:
            user = User.objects.get(pk=userid)
            follower_id = request.data.get("follower_id")
            if not follower_id:
                return Response({"error": "Follower ID is required"}, status=status.HTTP_400_BAD_REQUEST)
            user.Followers.append(follower_id)
            user.save()
            return Response({"message": "Follower added successfully"}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class PromptListView(APIView):
    def get(self, request):
        prompts = Prompt.objects.all()
        serializer = PromptSerializer(prompts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PromptSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutUserView(APIView):
    def post(self, request):
        logout(request)
        return redirect('login')  # Redirect to login page after logout

class LoginUserView(APIView):
    def post(self, request):
        username = request.data.get('Username')
        if username:
            user = User.objects.filter(Username=username).first()
        if not user:
            return Response({"error": "User not found."}, status=status.HTTP_400_BAD_REQUEST)
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UpdateVotesView(APIView):
    def post(self, request, post_id, vote_type):
        try:
            post = Post.objects.get(pk=post_id)  
        except Post.DoesNotExist:
            return Response({"error": "Post not found."}, status=status.HTTP_404_NOT_FOUND)

        if vote_type == 'upvote':
            post.UpvoteCount += 1  
        elif vote_type == 'downvote':
            post.DownvoteCount += 1  
        else:
            return Response({"error": "Invalid vote type. Use 'upvote' or 'downvote'."}, status=status.HTTP_400_BAD_REQUEST)

        post.save()  

        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class FollowUserView(APIView):
    def post(self, request, user_id):
        follower_user_id = request.data.get('follower_user_id')  

        if not follower_user_id:
            return Response({"error": "Follower user ID is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            target_user = User.objects.get(pk=user_id)  # Get the target user by ID
            follower_user = User.objects.get(pk=follower_user_id)  # Get the follower user by ID
        except User.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        # Check if the user is already following the target user
        if follower_user_id in target_user.Followers:
            return Response({"message": "You are already following this user."}, status=status.HTTP_200_OK)

        # Add the follower's user ID to the target user's followers list
        target_user.Followers.append(follower_user_id)
        target_user.save()

        return Response({"message": "User followed successfully."}, status=status.HTTP_200_OK)

class UnfollowUserView(APIView):
    def post(self, request, user_id):
        """
        Unfollow a user by removing the follower's user ID from the target user's followers list.
        """
        follower_user_id = request.data.get('follower_user_id')  # The ID of the user who wants to unfollow

        if not follower_user_id:
            return Response({"error": "Follower user ID is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            target_user = User.objects.get(pk=user_id)  # Get the target user by ID
            follower_user = User.objects.get(pk=follower_user_id)  # Get the follower user by ID
        except User.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        # Check if the user is following the target user
        if follower_user_id not in target_user.Followers:
            return Response({"message": "You are not following this user."}, status=status.HTTP_400_BAD_REQUEST)

        # Remove the follower's user ID from the target user's followers list
        target_user.Followers.remove(follower_user_id)
        target_user.save()

        return Response({"message": "User unfollowed successfully."}, status=status.HTTP_200_OK)

class GetFollowersView(APIView):
    def get(self, request, user_id):
        """
        Get the list of followers for a specific user.
        """
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        return Response({"followers": user.Followers}, status=status.HTTP_200_OK)

class RegisterUserView(APIView):
    def post(self, request):
        username = request.data.get('Username')
        if not username:
            return Response({"error": "Username is required."}, status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(Username=username).exists():
            return Response({"error": "A user with this username already exists."}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.create(
            Username=username,
            ProfilePicture=None,  # Default profile picture
            Bio="",
            ReplyPoints=0,
            Followers=[]  # Default empty followers list
        )
        user.save()
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED)