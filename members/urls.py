from django.urls import path
from .views import member_create_view, MemberListView

app_name = "members"

urlpatterns = [
    path("", MemberListView.as_view(), name="member_list"),
    path("new/", member_create_view, name="member"),
]
