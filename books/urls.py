from django.urls import path
from . import views

app_name = "books"

urlpatterns = [
    path("", views.BookListView.as_view(), name="book_list"),
    path("new/", views.book_create, name="book_create"),
    path("<slug:book_slug>/", views.book_detail, name="book_detail"),
    path("<slug:book_slug>/edit/", views.book_edit, name="book_edit"),
    path("<slug:book_slug>/delete/", views.book_delete, name="book_delete"),
]
