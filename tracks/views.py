from django.shortcuts import get_object_or_404, render

from .models import Track

def tracks(request, title):
    track = get_object_or_404(Track, title=title)
    return render(request, 'tracks.html', { 'track': track})
