from django.shortcuts import render, redirect

from orders.forms import OrderForm
from orders.models import Order


def order_create_view(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            Order.objects.order_create(**cleaned_data)
            return redirect("/")
    else:
        form = OrderForm()
    return render(request, "orders/order_form.html", {
        "form": form,
    })
