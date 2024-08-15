from django.urls import path
from django.contrib.auth.views import LogoutView
from users.views import login_request, register


urlpatterns = [
    path('login/', login_request, name='login'),
    path('register/', register, name='registro'),
    path('logout/', LogoutView.as_view(template_name='apppreentrega/inicio.html'), name="Logout")
    ]