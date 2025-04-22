from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from accounts.views import signup

class CustomLogoutView(LogoutView):
    http_method_names = ['get', 'post']  # Allow GET and POST requests
    template_name = "registration/logout.html"  # Use your custom logout.html page

urlpatterns = [
    path("login/", LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),  # Use the custom logout view
    path("signup/", signup, name="signup"),
]
