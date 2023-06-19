from .models import Post
from rest_framework import serializers
from apps.account.serializers import UserSerializer


class PostSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)


    class Meta:
        model = Post
        fields = ('id', 'body', 'created_by', 'createdAtFormater')