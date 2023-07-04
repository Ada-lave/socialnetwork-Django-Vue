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


from apps.post.models import Post, Trend


def hashtag(post, trends):
    

    for words in post.split():
        if words[0] == '#':
            print(words)
            trends.append(words[1:])
    
    return trends



trends = []

this_time = timezone.now().replace(minute=0, second=0, microsecond=0)
timer = this_time = timedelta(hours=12)

for trend in Trend.objects.all():
    trend.delete()

for post in Post.objects.all():
    # print(post.body)
    hashtag(post.body, trends)

trends_counter = Counter(trends).most_common(10)

for trend in trends_counter:
    Trend.objects.create(hashtag = trend[0], occurences=trend[1])



