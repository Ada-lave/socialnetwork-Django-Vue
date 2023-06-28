from .models import Conversition, ConversitionMessage
from rest_framework import serializers
from apps.account.serializers import UserSerializer

class ConversitionSerializer(serializers.ModelSerializer):
    users = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Conversition
        fields = ('id','users', 'modifiedAtFormater',)

class ConversitionMessageSerializer(serializers.ModelSerializer):
    sent_to = UserSerializer(read_only=True)
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = ConversitionMessage
        fields = ('id','sent_to','created_by','createdAtFormater','body',)

class ConversitionDetailSerializer(serializers.ModelSerializer):
    messages = ConversitionMessageSerializer(read_only=True, many=True)

    class Meta:
        model = Conversition
        fields = ('id','users', 'modifiedAtFormater','messages',)

