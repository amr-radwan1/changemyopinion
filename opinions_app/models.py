from django.db import models
from django.contrib.postgres.fields import ArrayField


class User(models.Model):
    UserID = models.AutoField(primary_key=True, db_column='userid')  
    Username = models.CharField(max_length=100, unique=True, db_column='username')
    Email = models.EmailField(unique=True, db_column='email')
    Password = models.CharField(max_length=255, db_column='password')
    ProfilePicture = models.CharField(max_length=200, null=True, db_column='profile_picture')
    JoinDate = models.DateTimeField(auto_now_add=True, db_column='join_date')
    Bio = models.TextField(null=True, db_column='bio')
    ReplyPoints = models.IntegerField(default=0, db_column='reply_points')
    Followers = ArrayField(models.IntegerField(), null=True, db_column='followers')  # Array of user IDs who follow this user

    class Meta:
        db_table = 'users'


class Post(models.Model):
    PostID = models.AutoField(primary_key=True, db_column='postid')
    UserID = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')  # Relating to User
    UpvoteCount = models.IntegerField(default=0, db_column='upvote_count')
    DownvoteCount = models.IntegerField(default=0, db_column='downvote_count')
    CreatedAt = models.DateTimeField(auto_now_add=True, db_column='created_at')

    class Meta:
        db_table = 'posts'


class Reply(models.Model):
    ReplyID = models.AutoField(primary_key=True, db_column='replyid')
    PostID = models.ForeignKey(Post, on_delete=models.CASCADE, db_column='post_id')  # Relating to Post
    UserID = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')  # Relating to User
    ReplyText = models.TextField(db_column='replytext')
    CreatedAt = models.DateTimeField(auto_now_add=True, db_column='created_at')

    class Meta:
        db_table = 'replies'
