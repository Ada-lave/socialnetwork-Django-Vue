from .models import Post, Comment
from rest_framework import serializers
from apps.account.serializers import UserSerializer


class PostSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)


    class Meta:
        model = Post
        fields = ('id', 'body', 'created_by','comments_count', 'createdAtFormater','likes_count')


class CommentSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ('id', 'body' , 'created_by','createdAtFormater',)


class PostDetailSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    comments = CommentSerializer(read_only=True)


    class Meta:
        model = Post
        fields = ('id', 'body', 'created_by', 'createdAtFormater','likes_count','comments', 'comments_count')