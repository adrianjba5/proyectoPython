from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate

def login_request (request):
        
        if request.method == "POST":
                form = AuthenticationForm(request, data = request.POST)       
        
        if form.is_valid():
                
                usuario = form.cleaned_data.get('username')
                contrasenia = form.cleaned_data.get('password')
                
                user = authenticate(username= usuario, password=contrasenia)
                
                if user:
                        login(request, user)
                        return render(request,"apppreentrega/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
                
        msg_login = "Usuario o contraseña incorrectos"
        
        form = AuthenticationForm()
        return render(request, "users/login.html", {"form":form,"msg_login": msg_login})
