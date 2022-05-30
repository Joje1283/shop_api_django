from django.urls import path
from .views import BookCreateView, BookDetailView, BookUpdateView

app_name = "items"

urlpatterns = [
    path("", BookDetailView.as_view(), name="detail_view"),
    path("new/", BookCreateView.as_view(), name="create_view"),
    path("<int:pk>/edit/", BookUpdateView.as_view(), name="update_view")
]