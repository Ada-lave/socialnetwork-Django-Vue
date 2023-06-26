from django.shortcuts import render
from django.http import JsonResponse
from .serializers import PostSerializer, PostDetailSerializer, CommentSerializer
from .models import Post, Like, Comment
from rest_framework.decorators import api_view
from .forms import PostForm
from apps.account.models import User
from apps.account.serializers import UserSerializer



@api_view(["GET"])
def postListAll(request):

    user_ids = [request.user.id]
    for user in request.user.friends.all():
        user_ids.append(user.id)

    posts = Post.objects.filter(created_by_id__in=list(user_ids))

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

@api_view(['POST'])
def postLike(request, pk):
    post = Post.objects.get(pk=pk)

    if not post.likes.filter(created_by=request.user):
        like = Like.objects.create(created_by=request.user)

        post.likes_count += 1
        post.likes.add(like)
        post.save()
        return JsonResponse({'message':'like append'})
    
    elif post.likes.filter(created_by=request.user):
        if post.likes_count !=0:
            post.likes_count -= 1
            post.save()
            return JsonResponse({'message':'like delete'})
        else:
            post.likes_count += 1
            post.save()
            return JsonResponse({'message':'like up'})

       
    return JsonResponse({'message':''})





@api_view(['GET'])
def postDetail(request, pk):
    post = Post.objects.get(pk=pk)


    return JsonResponse({
        'post': PostDetailSerializer(post).data
    }) 



@api_view(['POST'])
def postComment(request, pk):
    comment = Comment.objects.create(body=request.data.get('body'), created_by=request.user)

    post = Post.objects.get(pk=pk)
    post.comments.add(comment)
    post.comments_count = post.comments_count + 1
    post.save()

    serializer = CommentSerializer(comment)

    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def postDetailComment(request, pk):
    post = Post.objects.get(pk=pk)
    comments = post.comments
    serializer = CommentSerializer(comments, many=True)
    return JsonResponse(serializer.data, safe=False)