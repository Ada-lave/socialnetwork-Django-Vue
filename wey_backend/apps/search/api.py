from django.http import JsonResponse
from apps.post.serializers import PostSerializer
from apps.post.models import Post
from apps.account.models import User
from rest_framework.decorators import api_view
from apps.account.serializers import UserSerializer

@api_view(['POST'])
def search(request):

    data = request.data

    query = data['query']
    users = User.objects.filter(name__icontains=query)
    posts = Post.objects.filter(body__icontains=query)

    user_serializer = UserSerializer(users, many=True)
    post_serializer = PostSerializer(posts, many=True)


    return JsonResponse({'users':user_serializer.data,
                         'posts':post_serializer.data}, safe=False)
