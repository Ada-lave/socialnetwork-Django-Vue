from django.db import models
import uuid
from apps.account.models import User
from django.utils.timesince import timesince


class Conversition(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    users = models.ManyToManyField(User, related_name='беседа')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True) 

    def modifiedAtFormater(self):
        return timesince(self.created_at)

class ConversitionMessage(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    conversition = models.ForeignKey(Conversition, related_name='сообщение',  on_delete=models.CASCADE)
    body = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='отправитель', on_delete=models.CASCADE)
    sent_to = models.ForeignKey(User, related_name='получатель', on_delete=models.CASCADE)

    def createdAtFormater(self):
        return timesince(self.created_at)
