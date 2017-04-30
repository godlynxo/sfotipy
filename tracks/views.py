import json
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Track


def tracks(request, title):
    track = get_object_or_404(Track, title=title)
    data = {
        'title': track.title,
        'order': track.order,
        'track_file': track.track_file.url,
        'album': track.album.title,
        'artist': {
            'first_name': track.artist.first_name,
            'last_name': track.artist.last_name,
            'biography': track.artist.biography
        }
    }
    json_data = json.dumps(data)
    return HttpResponse(json_data, content_type='application/json')
