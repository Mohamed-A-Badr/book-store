from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm, ProfileForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

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

        return redirect("books:book_list")
    else:
        return render(request, "accounts/logout.html")


@login_required
def profile_view(request):
    user = get_object_or_404(User, id=request.user.id)

    return render(
        request,
        "accounts/profile.html",
        {
            "user": user,
        },
    )


@login_required
def edit_profile_view(request):
    user = get_object_or_404(User, id=request.user.id)
    form = ProfileForm(instance=user)
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("profile")
    return render(
        request,
        "accounts/profile_edit.html",
        {
            "form": form,
        },
    )
