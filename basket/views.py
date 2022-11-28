from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User

from products.models import Product
from profiles.models import UserProfile


def view_basket(request):
    """ A view to render the bage contents """
    profile = None
    user = request.user

    if user.id is None:
        return render(request, 'basket/basket.html')
    else:
        profile = get_object_or_404(UserProfile, user=request.user)
        context = {
            'profile': profile,
        }

    return render(request, 'basket/basket.html', context)


def add_to_basket(request, item_id):
    """ A view to add items to the basket """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
        messages.success(request, f'Quantity changed for {product.title} to {quantity} in your basket')
    else:
        basket[item_id] = quantity
        messages.success(request, f'Added {product.title} to your basket')

    request.session['basket'] = basket
    return redirect(redirect_url)


def adjust_basket(request, item_id):
    """ Adjust the qty of a specified product by the specified amount """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})
    
    if quantity > 0:
        basket[item_id] = quantity
        messages.success(request, f'Quantity updated for {product.title} to {quantity} in your basket')
    else:
        basket.pop[item_id]
        messages.success(request, f'Removed {product.title} from your basket')

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def remove_from_basket(request, item_id):
    """ A view to remove a specified item from the basket """

    product = get_object_or_404(Product, pk=item_id)
    basket = request.session.get('basket', {})
    try:
        basket.pop(item_id)
        messages.success(request, f'Removed {product.title} from your basket')

        request.session['basket'] = basket
        return HttpResponse(status=200)
    
    except Exception as e:
        messages.error(request, f'Error removing items: {e}')
        return HttpResponse(status=500)
