from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Member


class MemberForm(forms.ModelForm):
    class Meta(UserCreationForm.Meta):
        model = Member
        fields = ['username', 'email', 'first_name', 'last_name', 'city', 'street', 'zipcode', 'password']
