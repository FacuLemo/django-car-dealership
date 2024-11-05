from users.models import Profile
from django.utils.translation import (
    activate
)

def locale(get_response):
    def middleware(request):
        if request.user.is_authenticated:
            profile = Profile.objects.filter(user=request.user).first()
            if profile:
                lang = profile.lang
                activate(lang)
        response = get_response(request)
        
        return response

    return middleware