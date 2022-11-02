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
        'stripe_public_key': 'pk_test_51LzhQUHjG9DDmtCup63DaDHDKfyuoVEz5JInhFA1IV2mMve56TH8ElBjrienWZlC3atyv3o2gnBP4mv1WnYjBTkI00yT4kjIcd',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
