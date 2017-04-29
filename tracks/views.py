from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .models import Track

def tracks(request, title):
    track = get_object_or_404(Track, title=title)
    return HttpResponse(track)
