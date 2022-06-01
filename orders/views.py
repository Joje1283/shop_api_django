from django.db.models import Prefetch
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView

from items.exceptions import NotEnoughStockException
from orders.forms import OrderForm, SearchForm
from orders.models import Order


def order_create_view(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            try:
                Order.objects.order_create(**cleaned_data)
            except NotEnoughStockException as e:
                # 장고에서는 Form에서 체크하는게 알맞아 보인다.
                messages.info(request, e, "danger")
                return render(request, "orders/order_form.html", {"form": form})
            return redirect("/orders")
    else:
        form = OrderForm()
    return render(request, "orders/order_form.html", {
        "form": form,
    })


class OrderListView(ListView):
    model = Order
    template_name = "orders/order_list.html"
    form_class = SearchForm
    queryset = Order.objects.all().select_related("member")

    def get_queryset(self):
        form = self.form_class(self.request.GET)
        qs = super(OrderListView, self).get_queryset()
        if form.is_valid():
            member_name, status = form.cleaned_data.values()
            if member_name:
                qs = qs.filter(member__username__icontains=member_name)
            if status:
                qs = qs.filter(status=status)
        return qs

    def get_context_data(self, **kwargs):
        context = super(OrderListView, self).get_context_data()
        context['form'] = self.form_class
        return context


@csrf_exempt
def order_cancel_view(request, order_id):
    order = Order.objects.get(pk=order_id)
    order.cancel()
    return redirect("/orders")
