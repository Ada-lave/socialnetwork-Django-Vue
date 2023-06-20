from django.shortcuts import render
from django.http import JsonResponse
from .serializers import PostSerializer
from .models import Post
from rest_framework.decorators import api_view
from .forms import PostForm
from apps.account.models import User
from apps.account.serializers import UserSerializer


@api_view(["GET"])
def postListAll(request):
    posts = Post.objects.all()

    serializer = PostSerializer(posts, many=True)

    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def postListUser(request, id):
    user = User.objects.get(pk=id)
    posts = Post.objects.filter(created_by=id)

    post_serializer = PostSerializer(posts, many=True)
    user_serializer = UserSerializer(user)

    return JsonResponse({'posts':post_serializer.data,
                        'user':user_serializer.data}, safe=False)


@api_view(["POST"])
def addPost(request):
    data = request.data

    form = PostForm(request.data)

    if form.is_valid():
        post = form.save(commit=False)
        post.created_by = request.user
        post.save()

        serializer = PostSerializer(post)
        return JsonResponse(serializer.data, safe=False)

    return JsonResponse({'message':'cant add post'})

