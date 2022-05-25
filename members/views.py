from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView, UpdateView, ListView

from .forms import MemberForm
from .models import Member


def member_create_view(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            Member.objects.join(**cleaned_data)
            return redirect("/")
    else:
        form = MemberForm()
    return render(request, 'members/member_form.html', {
        'form': form,
    })


class MemberListView(ListView):
    model = Member
