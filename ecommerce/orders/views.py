from django.shortcuts import render, HttpResponse, redirect
from carts.models import CartItem
from orders.models import Order
from .forms import OrderForm

# Create your views here.


def place_order(request):
    current_user = request.user

    # if the cart count is less then or equal to zero, then redirect back to shop
    cart_items = CartItem.objects.filter(user=current_user)
    cart_counts = cart_items.count()
    if cart_counts <= 0:
        return redirect('store')

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # store all the billing information inside order table
            data = Order()
            data.first_name = form.cleaned_data('first_name')
            data.last_name = form.cleaned_data('last_name')
            data.phone = form.cleaned_data('phone')
            data.email = form.cleaned_data('email')
            data.address_line_1 = form.cleaned_data('address_line_1')
            data.address_line_2 = form.cleaned_data('address_line_2')
            data.country = form.cleaned_data('country')
            data.state = form.cleaned_data('state')
            data.city = form.cleaned_data('city')
            data.order_note = form.cleaned_data('order_note')
