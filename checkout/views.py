from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from bag.contexts import bag_contents

import stripe


def checkout(request):
    """
    View for checkout from shopping bag
    """
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(
            request, "You haven't added any products yet!")
        return redirect(reverse('products'))

    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51LzhQUHjG9DDmtCup63DaDHDKfyuoVEz5JInhFA1IV2mMve56TH8ElBjrienWZlC3atyv3o2gnBP4mv1WnYjBTkI00yT4kjIcd',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
