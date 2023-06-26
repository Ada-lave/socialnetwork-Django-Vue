from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .models import Conversition, ConversitionMessage
from .serializers import *

from .serializers import *

api_view(['GET'])
def conversitionList(request):
    conversition = Conversition.objects.filter(users__in=list([request.user.id]))
    print(request.user.id)
    serializer = ConversitionSerializer(conversition)
    return JsonResponse(serializer.data, safe=False)
    
