from django.shortcuts import render
from .models import SocialMedia
# Create your views here.


def social_media(request):
    socials = SocialMedia.objects
    return render(request, 'social_media/social_media.html', {'socials': socials})
