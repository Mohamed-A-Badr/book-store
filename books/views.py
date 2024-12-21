from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Book


# Create your views here.
class BookListView(ListView):
    model = Book
    template_name = "books/book_list.html"
    context_object_name = "books"


def book_detail(request, book_slug):
    book = get_object_or_404(Book, slug=book_slug)

    return render(
        request,
        "books/book_detail.html",
        {"book": book},
    )
