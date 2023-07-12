from django.db import models
import uuid
from apps.account.models import User
from django.utils.timesince import timesince
from apps.post.models import Post


class Notification(models.Model):
    NEWFRIENDREQUEST = 'newfriendrequest'
    ACCEPTEDFRIENDREQUEST = 'acceptedfriendrequest'
    REJECTEDFRIENDREQUEST = 'rejectedfriendrequest'
    POST_LIKE = 'postlike'
    POST_COMMENT = 'postcomment'

    CHOISES_TYPE = (
        (NEWFRIENDREQUEST,'new friend'),
        (ACCEPTEDFRIENDREQUEST, 'accepted friend'),
        (REJECTEDFRIENDREQUEST,'rejected friend'),
        (POST_LIKE,'post like'),
        (POST_COMMENT,'post comment')
    )



    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    post = models.ForeignKey(Post, blank=True, null=True, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='created_notif', on_delete=models.CASCADE)
    created_for = models.ForeignKey(User, related_name='reciver', on_delete=models.CASCADE)
    body = models.TextField()
    is_read = models.BooleanField(default=False)
    type = models.CharField(choices=CHOISES_TYPE, max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def createdAtFormater(self):
        return timesince(self.created_at)
