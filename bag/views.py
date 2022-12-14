from django.shortcuts import render, redirect, reverse, HttpResponse, \
    get_object_or_404
from django.contrib import messages

from products.models import Product


def view_bag(request):
    """
    A view to render the shopping bag template
    """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """
    A view to add product and quantity to the bag view
    """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(
            request, f'''Updated {product.watch_model} quantity
            to {bag[item_id]} products in your bag.''')
    else:
        bag[item_id] = quantity
        messages.success(
            request, f'{product.watch_model}, added to your shopping bag!')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """
    A view to adjust the quantity of a specific
    product in shopping bag
    """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(
            request, f'''Updated {product.watch_model}
            quantity to {bag[item_id]}!''')
    else:
        bag.pop(item_id)
        messages.success(
            request, f'Removed {product.watch_model} from your bag!')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """
    A view to remove a item from the shopping bag
    """
    try:
        product = get_object_or_404(Product, pk=item_id)
        bag = request.session.get('bag', {})

        bag.pop(item_id)
        messages.success(
            request, f'Removed {product.watch_model} from your bag!')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
