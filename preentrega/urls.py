from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/',admin.site.urls),
    path("inicio",include("apppreentrega.urls")),
    path("users/",include("users.urls")),
    ]
