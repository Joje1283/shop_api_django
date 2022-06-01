from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include


def root(request):
    return render(request, "root.html")


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", root, name="root"),
    path("members/", include("members.urls")),
    path("items/", include("items.urls")),
    path("orders/", include("orders.urls")),
    path('__debug__/', include('debug_toolbar.urls')),
]
