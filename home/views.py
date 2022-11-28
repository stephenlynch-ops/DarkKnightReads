from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from profiles.models import UserProfile


def index(request):
    """ A view to open the home page """
    user=request.user

    if user.id == None:

        return render(request, 'home/index.html')
    
    else:
        profile = get_object_or_404(UserProfile, user=request.user)
        context = {
            'profile': profile,
        }

        return render(request, 'home/index.html', context)
    
