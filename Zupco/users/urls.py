from django.urls import path, include
from users.views import dashboard, register, login_view

urlpatterns = [
    path('', login_view, name="welcome"),  # Map root URL to login view
    path("accounts/", include("django.contrib.auth.urls")),
    path("dashboard/", dashboard, name="dashboard"),
    path("register/", register, name="register"),
]
