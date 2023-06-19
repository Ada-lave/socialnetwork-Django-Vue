from django.shortcuts import render
from django.http import JsonResponse
from .serializers import PostSerializer
from .models import Post
from rest_framework.decorators import api_view
from .forms import PostForm


@api_view(["GET"])
def postListAll(request):
    posts = Post.objects.all()

    serializer = PostSerializer(posts, many=True)

    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def postListUser(request, id):
    posts = Post.objects.filter(created_by=id)

    serializer = PostSerializer(posts, many=True)

    return JsonResponse(serializer.data, safe=False)


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

