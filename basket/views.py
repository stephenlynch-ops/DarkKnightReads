from django.shortcuts import render


def view_basket(request):
    """ A view to render the bage contents """

    return render(request, 'basket/basket.html')
