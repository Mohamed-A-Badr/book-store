from django.urls import path
from . import views
from django.contrib.auth import views as auth_view


urlpatterns = [
    path("", views.profile_view, name="profile"),
    path("edit/", views.edit_profile_view, name="profile_edit"),
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path(
        "password-reset/", auth_view.PasswordResetView.as_view(), name="password_reset"
    ),
    path(
        "password-reset/done/",
        auth_view.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "password-reset/<uidb64>/<token>/",
        auth_view.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "password-reset/complete/",
        auth_view.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
]
