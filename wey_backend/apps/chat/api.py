from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .models import Conversition, ConversitionMessage
from .serializers import *

from apps.post.models import Post
from apps.post.serializers import PostSerializer


@api_view(["GET"])
def conversitionList(request):
    conv = Conversition.objects.filter(users__in=list([request.user]))
    print(conv)
    serializer = ConversitionSerializer(conv, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(["GET"])
def conversitionDetail(request,pk):
    conv = Conversition.objects.filter(users__in=list([request.user])).get(pk=pk)
    message = ConversitionMessage.objects.filter(conversition=conv)
    serializer = ConversitionDetailSerializer(conv)
    

    return JsonResponse(serializer.data, safe=False)

@api_view(['POST'])
def conversitionSendMessage(request,pk):
    conv = Conversition.objects.filter(users__in=list([request.user])).get(pk=pk)

    for user in conv.users.all():
        if user!=request.user:
            sent_to = user
             
    conv_message = ConversitionMessage.objects.create(conversition=conv, body=request.data.get('body'),\
                                                      created_by = request.user, sent_to = sent_to)
    
    serializer = ConversitionMessageSerializer(conv_message)

    return JsonResponse(serializer.data, safe=False)
       


