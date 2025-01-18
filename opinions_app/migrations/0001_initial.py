# Generated by Django 5.1.3 on 2025-01-18 08:58

import django.contrib.postgres.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prompt',
            fields=[
                ('PromptID', models.AutoField(db_column='promptid', primary_key=True, serialize=False)),
                ('PromptText', models.TextField(db_column='prompt_text')),
                ('Category', models.TextField(db_column='category')),
            ],
            options={
                'db_table': 'prompts',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('UserID', models.AutoField(db_column='userid', primary_key=True, serialize=False)),
                ('Username', models.CharField(db_column='username', max_length=100, unique=True)),
                ('Email', models.EmailField(db_column='email', max_length=254, unique=True)),
                ('Password', models.CharField(db_column='password', max_length=255)),
                ('ProfilePicture', models.CharField(db_column='profile_picture', max_length=200, null=True)),
                ('JoinDate', models.DateTimeField(auto_now_add=True, db_column='join_date')),
                ('Bio', models.TextField(db_column='bio', null=True)),
                ('ReplyPoints', models.IntegerField(db_column='reply_points', default=0)),
                ('Followers', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), db_column='followers', null=True, size=None)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('PostID', models.AutoField(db_column='postid', primary_key=True, serialize=False)),
                ('UpvoteCount', models.IntegerField(db_column='upvote_count', default=0)),
                ('DownvoteCount', models.IntegerField(db_column='downvote_count', default=0)),
                ('CreatedAt', models.DateTimeField(auto_now_add=True, db_column='created_at')),
                ('PostText', models.TextField(db_column='posttext')),
                ('PromptID', models.ForeignKey(db_column='prompt_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='opinions_app.prompt')),
                ('UserID', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to='opinions_app.user')),
            ],
            options={
                'db_table': 'posts',
            },
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('ReplyID', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('ReplyText', models.TextField(db_column='replytext')),
                ('CreatedAt', models.DateTimeField(auto_now_add=True, db_column='created_at')),
                ('isAgree', models.BooleanField(db_column='isagree', default=None)),
                ('PostID', models.ForeignKey(db_column='post_id', on_delete=django.db.models.deletion.CASCADE, to='opinions_app.post')),
                ('UserID', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to='opinions_app.user')),
            ],
            options={
                'db_table': 'replies',
            },
        ),
    ]
