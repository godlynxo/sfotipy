from django.http import HttpResponse, Http404
from django.shortcuts import render

from .models import Track

def tracks(request, title):
    try:
        track = Track.objects.get(title=title)
    except Track.DoesNotExist:
        raise Http404
    return HttpResponse(track)
