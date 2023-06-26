from django.urls import path
from .api import postListAll, postListUser, postLike, postDetail, addPost, postComment
urlpatterns = [
    path('', postListAll, name='allPosts'),
    path('createPost/', addPost, name='addPost'),
    path('userAllPosts/<uuid:id>', postListUser, name='postListUser'),
    path('<uuid:pk>/comment/', postComment,name='postComment'),
    path('<uuid:pk>/like/', postLike, name='postLike'),
    path('<uuid:pk>/', postDetail, name='postDetail'),



]