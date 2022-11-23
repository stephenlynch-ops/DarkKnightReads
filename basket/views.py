from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product


def view_basket(request):
    """ A view to render the bage contents """

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ A view to add items to the basket """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
    else:
        basket[item_id] = quantity

    request.session['basket'] = basket
    return redirect(redirect_url)


def adjust_basket(request, item_id):
    """ Adjust the qty of a specified product by the specified amount """

    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})
    
    if quantity > 0:
        basket[item_id] = quantity
    else:
        basket.pop[item_id]

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def remove_from_basket(request, item_id):
    """ A view to remove a specified item from the basket """

    basket = request.session.get('basket', {})
    try:
        basket.pop(item_id)

        request.session['basket'] = basket
        return HttpResponse(status=200)
    
    except Exception as e:
        return HttpResponse(status=500)
