# -*- coding: utf-8 -*-
import django
import os
import sys
from collections import Counter
from django.utils import timezone
from datetime import timedelta

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)),'..'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE","wey_backend.settings")
django.setup()


from apps.account.models import User

users = User.objects.all()

for user in users:
    user.people_you_may_know.clear()
    print(f'{user.name} Friends:')

    for friend in user.friends.all():
        print(friend.name)
        for friendreq in friend.friends.all():
            if friendreq not in user.friends.all() and  friendreq != user:
                print(f'Можно добавить {friendreq.name}')
                user.people_you_may_know.add(friendreq)
    print()