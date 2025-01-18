from django.db import models
from django.contrib.postgres.fields import ArrayField


class User(models.Model):
    UserID = models.AutoField(primary_key=True, db_column='userid')  
    Username = models.CharField(max_length=100, unique=True, db_column='username')
    Email = models.EmailField(unique=True, db_column='email')
    Password = models.CharField(max_length=255, db_column='password')
    DisplayName = models.CharField(max_length=255, null=True, db_column='displayname')
    ChatID = ArrayField(models.IntegerField(), null=True, db_column='chatid')
    isInfluencer = models.BooleanField(default=False, db_column='isinfluencer')

    class Meta:
        db_table = 'users'


class Post(models.Model):
    PostID = models.AutoField(primary_key=True, db_column='postid')
    UserID = models.ForeignKey(User, on_delete=models.CASCADE, db_column='userid')  # Relating to User
    UpvoteCount = models.IntegerField(default=0, db_column='upvotecount')
    DownvoteCount = models.IntegerField(default=0, db_column='downvotecount')
    CreatedAt = models.DateTimeField(auto_now_add=True, db_column='createdat')

    class Meta:
        db_table = 'posts'


class Reply(models.Model):
    ReplyID = models.AutoField(primary_key=True, db_column='replyid')
    PostID = models.ForeignKey(Post, on_delete=models.CASCADE, db_column='postid')  # Relating to Post
    UserID = models.ForeignKey(User, on_delete=models.CASCADE, db_column='userid')  # Relating to User
    ReplyText = models.TextField(db_column='replytext')
    CreatedAt = models.DateTimeField(auto_now_add=True, db_column='createdat')

    class Meta:
        db_table = 'replies'


class Follower(models.Model):
    ID = models.AutoField(primary_key=True, db_column='id')
    FollowerID = models.ForeignKey(User, on_delete=models.CASCADE, db_column='followerid')
    FollowedID = models.ForeignKey(User, on_delete=models.CASCADE, db_column='followedid')  # Made nullable

    class Meta:
        db_table = 'followers'

