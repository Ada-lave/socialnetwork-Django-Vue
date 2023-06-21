from django.http import JsonResponse
from . import forms
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .models import User, FriendshipRequest

from .serializers import UserSerializer, FriendshipRequestSerializer

@api_view(["POST"])
@authentication_classes([])
@permission_classes([])
def signup(request):
    data = request.data
    message = 'success'

    form = forms.SignupForm({
        'email': data.get('email'),
        'name': data.get('name'),
        'password1': data.get('password1'),
        'password2': data.get('password2'),
    })

    if form.is_valid():
        form.save()
    else:
        message = 'error'

    return JsonResponse({'message':message})



@api_view(['GET'])
def informationAboutUser(request):
    return JsonResponse({
        'id': request.user.id,
        'email': request.user.email,
        'name': request.user.name,                
        })


@api_view(['GET'])
def friendsRequest(reqeust, pk):
    user = User.objects.get(pk=pk)

    if user == reqeust.user:
        reqeusts = FriendshipRequest.objects.filter(created_for=reqeust.user)

    friends = user.friends.all()

    return JsonResponse({
        'user': UserSerializer(user).data,
        'friends': UserSerializer(friends, many=True).data,
        'requests': FriendshipRequestSerializer(reqeusts, many=True).data
    })




@api_view(['POST'])
def sendFriendshipRequest(request, pk):

    user = User.objects.get(pk=pk)

    friendship = FriendshipRequest.objects.create(created_for=user, created_by = request.user)






    return JsonResponse({'message':'user in ship'})