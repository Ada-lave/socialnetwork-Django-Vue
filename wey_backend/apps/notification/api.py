from .serializers import NotificationSerializer
from django.http import JsonResponse
from .models import Notification
from rest_framework.decorators import api_view


@api_view(['GET'])
def notification(request):
    reciver = request.user.reciver.filter(is_read=False)
    serializer = NotificationSerializer(reciver, many=True)

    return JsonResponse(serializer.data, safe=False)

@api_view(['POST'])
def readNotification(request,pk):
    notification = Notification.objects.filter(created_for=request.user).get(pk=pk)
    notification.is_read = True
    notification.save()
    print('readasdasdasd')

    return JsonResponse({'message':'noti is read'})