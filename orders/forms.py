from django import forms
from members.models import Member
from items.models import Item


class OrderForm(forms.Form):
    member_id = forms.ModelChoiceField(Member.objects.all(), label="주문회원")
    item_id = forms.ModelChoiceField(Item.objects.all(), label="상품명")
    count = forms.IntegerField(label="주문수량")

    def clean(self):
        cleaned_data = {}
        result = super(OrderForm, self).clean()
        for k, v in result.items():
            if not isinstance(v, int):
                cleaned_data[k] = v.pk
            else:
                cleaned_data[k] = v
        return cleaned_data


class SearchForm(forms.Form):
    member_name = forms.CharField()
    status_choices = (
        ("O", "주문됨"),
        ("C", "취소됨"),
    )
    status = forms.ChoiceField(choices=status_choices)
