from django.urls import path
from . import views

app_name = "books"

urlpatterns = [
    path("", views.BookListView.as_view(), name="book_list"),
    path("<slug:book_slug>/", views.book_detail, name="book_detail"),
]
