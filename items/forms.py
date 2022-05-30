from django import forms

from .models import Item


class BookForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ["name", "price", "stock_quantity", "author", "isbn"]
