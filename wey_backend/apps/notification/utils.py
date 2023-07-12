from .models import Notification
from apps.post.models import Post
from apps.account.models import FriendshipRequest

def createNotification(request, type, post_id=None, friendreq_id=None):
    created_for = None
    body = ''
    post=None
    

    if type =='postlike':
        body = f'{request.user.name} оценил ваш пост'
        post = Post.objects.get(pk=post_id)
        created_for = post.created_by
    elif type == 'postcomment':
        body = f'{request.user.name} прокомментировал ваш пост'
        post = Post.objects.get(pk=post_id)
        created_for = post.created_by
    elif type == 'newfriendrequest':
        body = f'{request.user.name} хочет добавить вас в друзья'
        friendreq = FriendshipRequest.objects.get(pk=friendreq_id)
        created_for = friendreq.created_for
    elif type == 'acceptedfriendrequest':
        body = f'{request.user.name} принял ваш запрос в друзья'
        friendreq = FriendshipRequest.objects.get(pk=friendreq_id)
        created_for = friendreq.created_for
    elif type == 'rejectedfriendrequest':
        body = f'{request.user.name} отклонил ваш запрос в друзья'
        friendreq = FriendshipRequest.objects.get(pk=friendreq_id)
        created_for = friendreq.created_for


    notification = Notification.objects.create(
        created_by = request.user,
        body=body,
        created_for = created_for,
        post=post,
        type=type) 
    
    return notification