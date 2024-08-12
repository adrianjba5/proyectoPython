from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import path
from apppreentrega import views


urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("/listar/", views.CursoListView.as_view(), name="ListarClientes"),
    path("/crear/", views.CursoCreateListView.as_view(), name="CrearClientes"),
    path("/actualizar/<pk>/", views.CursoUpdateView.as_view(), name="ActualizarClientes"),
    path("/borrar/<pk>/", views.CursoDeleteView.as_view(), name="BorrarClientes"),
    

    
]
