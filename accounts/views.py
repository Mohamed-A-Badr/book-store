from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

# Create your views here.


def register_view(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect(
                "books:book_list",
            )
    return render(
        request,
        "accounts/register.html",
        {
            "form": form,
        },
    )


def login_view(request):
    error_message = None
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = (
                request.POST.get("next") or request.GET.get("next") or "books:book_list"
            )
            return redirect(next_url)
        else:
            error_message = "Invalid credentials."
    return render(
        request,
        "accounts/login.html",
        {
            "error": error_message,
        },
    )


def logout_view(request):
    if request.method == "POST":
        logout(request)

        return redirect("login")
    else:
        return render(request, "accounts/logout.html")
