from django.shortcuts import render


def index(request):
    """ A view to open the home page """

    return render(request, 'home/index.html')
