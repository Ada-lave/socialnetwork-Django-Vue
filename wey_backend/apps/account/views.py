from django.shortcuts import render
from .models import User
from django.http import HttpResponse



def activateEmail(request):
    email = request.GET.get('email','')
    id = request.GET.get('id','')

    if email and id:
        user = User.objects.get(email=email,id=id)
        print(user)

        user.is_active = True
        user.save()

        return HttpResponse('Ваш аккаунт активирован')