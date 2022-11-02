from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    """
    View for checkout from shopping bag
    """
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(
            request, "You haven't added any products yet!")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)
