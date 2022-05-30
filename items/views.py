from django.views.generic import CreateView, ListView, UpdateView

from items.forms import BookForm
from items.models import Item


class BookCreateView(CreateView):
    model = Item
    form_class = BookForm
    template_name = "items/item_form.html"
    success_url = "/"


class BookDetailView(ListView):
    model = Item
    template_name = "items/item_list.html"


class BookUpdateView(UpdateView):
    model = Item
    form_class = BookForm
    template_name = "items/item_form.html"
    success_url = "/"
