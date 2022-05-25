from django.urls import path
from .views import member_create_view

app_name = "members"

urlpatterns = [
    path("new/", member_create_view, name="member"),
]
