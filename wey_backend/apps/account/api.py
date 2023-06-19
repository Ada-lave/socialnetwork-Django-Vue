from django.http import JsonResponse
from . import forms
from rest_framework.decorators import api_view, authentication_classes, permission_classes

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