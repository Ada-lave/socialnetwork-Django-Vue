from .models import Post, Comment, Trend, PostAttachment
from rest_framework import serializers
from apps.account.serializers import UserSerializer

class PostAttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostAttachment
        fields = ('getImage','id')


class PostSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    attachments = PostAttachmentSerializer(read_only=True, many=True)

    class Meta:
        model = Post
        fields = ('id', 'body', 'created_by','comments_count', 'createdAtFormater','likes_count','attachments')


class CommentSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ('id', 'body' , 'created_by','createdAtFormater',)


class PostDetailSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    comments = CommentSerializer(read_only=True)
    attachments = PostAttachmentSerializer(read_only=True, many=True)


    class Meta:
        model = Post
        fields = ('id', 'body', 'created_by', 'createdAtFormater','likes_count','comments', 'comments_count','attachments')

class TrendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trend
        fields = '__all__'