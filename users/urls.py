from django.urls import path
from django.contrib.auth.views import LogoutView
from users import views


urlpatterns = [
    path('login/', views.login_request, name="Login"),
    path('register/', views.register, name = 'registro'),
    path('logout/', LogoutView.as_view(template_name='apppreentrega/inicio.html'), name="Logout")
    ]