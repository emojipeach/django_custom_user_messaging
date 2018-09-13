from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    # user signup
    path(
        'signup/',
        views.signup,
        name='signup'
        ),
    # user login
    path(
        'login/',
        LoginView.as_view(template_name='users/login.html'),
        name='login'
        ),
    # user self password change
    path(
        'password_change/',
        views.password_change,
        name='password_change'
        ),
]