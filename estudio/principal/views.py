from django.shortcuts import render, redirect
from .models import Usuario
from django.contrib.auth.models import User

def base(request):
    return render(request, 'principal/base.html')
def lista_usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'principal/lista_usuarios.html', {'usuarios': usuarios})

def crear_usuario(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        email = request.POST['email']
        
        # Crea un nuevo usuario
        user = User.objects.create_user(username=email, first_name=nombre, last_name=apellido, email=email)
        user.set_password('contraseña')
        user.save()
        
        # Redirecciona a la página de inicio
        return redirect('lista_usuarios')
    
    return render(request, 'principal/crear_usuario.html')


