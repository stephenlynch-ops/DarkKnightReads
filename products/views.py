from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib.auth.models import User
from .models import Product, Category
from .forms import ProductForm
from profiles.models import UserProfile

# Create your views here.


def all_products(request):
    """ A view to show all products, including searches and sorting """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None
    profile = None
    user = request.user

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            query = request.GET['category']
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'hero' in request.GET:
            query = request.GET['hero']

            queries = Q(title__icontains=query) | Q(hero__icontains=query)
            products = products.filter(queries)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(title__icontains=query) | Q(about_title__icontains=query) | Q(hero__icontains=query) | Q(author__icontains=query) | Q(about_author__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    if user.id == None:
        context = {
                    'products': products,
                    'search_term': query,
                    'current_categories': categories,
                    'current_sorting': current_sorting,
                }
    else:
        profile = get_object_or_404(UserProfile, user=request.user)
    
        context = {
            'products': products,
            'search_term': query,
            'current_categories': categories,
            'current_sorting': current_sorting,
            'profile': profile,
        }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show the selected products detail """

    product = get_object_or_404(Product, pk=product_id)

    profile = get_object_or_404(UserProfile, user=request.user)

    context = {
        'product': product,
        'profile': profile,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'The new product has been added to the store')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, "Your new product couldn't be added at this time. Please check the form for errors")
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit an existing product in the store """
    profile = get_object_or_404(UserProfile, user=request.user)

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully updated {product.title}!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please check the form for errors')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.title}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
        'profile': profile,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
