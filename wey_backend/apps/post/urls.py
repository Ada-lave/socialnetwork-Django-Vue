from django.urls import path
from .api import postListAll, addPost, postListUser, postLike
urlpatterns = [
    path('', postListAll, name='allPosts'),
    path('createPost/', addPost, name='addPost'),
    path('userAllPosts/<uuid:id>', postListUser, name='postListUser'),
    path('<uuid:pk>/like/', postLike)

]