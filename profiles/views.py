from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views import View, generic

from django.contrib.auth.models import User

from .models import UserProfile, FavouriteWatch
from .forms import UserProfileForm

from checkout.models import Order
from products.models import Product


@login_required
def profile(request):
    """
    A view to display the user's profile page
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your Profile was updated successfully!')
        else:
            messages.error(
                request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True,
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


class AllFavourites(generic.ListView):
    """
    Render favourite.html template for user
    """
    model = Product
    template_name = 'profiles/favourite.html'

    def get_queryset(self, *args, **kwargs):
        queryset = FavouriteWatch.objects.filter(user=self.request.user)
        return queryset


def add_favorite_watch(request, product_id):
    """
    Add favorite watch to wish list
    """
    current_user = request.user
    current_watch = get_object_or_404(Product, pk=product_id)
    FavouriteWatch.objects.get_or_create(
        user=current_user, favourite_watch=current_watch)
    messages.success(request, (f"{current_watch.watch_model}, has been added \
        to your wish list."))
    return redirect(reverse('product_detail', args=[current_watch.id]))
