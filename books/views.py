from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.views.generic import ListView
from .models import Book
from .forms import BookForm
from django.utils.text import slugify


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


def book_create(request):
    form = BookForm()
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data

            new_book = form.save(commit=False)
            new_book.author = request.user
            new_book.slug = slugify(cd["title"])

            new_book.save()

            return redirect("books:book_list")

    return render(
        request,
        "books/book_create.html",
        {"form": form},
    )
