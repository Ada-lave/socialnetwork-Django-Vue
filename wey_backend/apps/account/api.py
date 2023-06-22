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
    reqeusts = []

    if user == reqeust.user:
        reqeusts = FriendshipRequest.objects.filter(created_for=reqeust.user, status=FriendshipRequest.SENT)
        reqeusts = FriendshipRequestSerializer(reqeusts, many=True)
        reqeusts = reqeusts.data

    friends = user.friends.all()

    return JsonResponse({
        'user': UserSerializer(user).data,
        'friends': UserSerializer(friends, many=True).data,
        'requests': reqeusts
    })




@api_view(['POST'])
def sendFriendshipRequest(request, pk):

    user = User.objects.get(pk=pk)

    check1 = FriendshipRequest.objects.filter(created_for=request.user).filter(created_by=user)
    check2 = FriendshipRequest.objects.filter(created_for=user).filter(created_by=request.user)

    if not check1 or not check2:
        FriendshipRequest.objects.create(created_for=user, created_by = request.user)
        return JsonResponse({'message':'user add ship'})
    else:
         return JsonResponse({'message':'user alredy in ship'})

@api_view(['POST'])
def handleRequest(request, id, status):
    user = User.objects.get(pk=id)
    req_user = request.user

    friendship = FriendshipRequest.objects.filter(created_for=request.user).get(created_by=user)
    friendship.status = status
    friendship.save()

    if status=='accepted':
        user.friends.add(request.user)
        user.friends_count += 1
        user.save()

        req_user.friends_count += 1
        req_user.save()

    return JsonResponse({'message':f" {request.user.name}: {user.name} {status}"})
    