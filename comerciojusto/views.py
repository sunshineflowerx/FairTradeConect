from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Perfil

def index(request):
    return render(request, 'comerciojusto/index.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        user = authenticate(username=email, password=senha)
        if user:
            login(request, user)
            return redirect('pos_login')
        return render(request, 'comerciojusto/login.html', {'erro': 'Credenciais inválidas'})
    return render(request, 'comerciojusto/login.html')

def cadastro_view(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        tipo = request.POST.get('tipo')

        if User.objects.filter(username=email).exists():
            return render(request, 'comerciojusto/cadastro.html', {'erro': 'Usuário já existe'})

        user = User.objects.create_user(username=email, email=email, password=senha, first_name=nome)
        Perfil.objects.create(user=user, tipo=tipo)
        return redirect('login')
    return render(request, 'comerciojusto/cadastro.html')

def logout_view(request):
    logout(request)
    return redirect('index')

@login_required(login_url='login')
def pos_login(request):
    perfil = Perfil.objects.get(user=request.user)
    if perfil.tipo == 'produtor':
        return redirect('area_produtor')
    elif perfil.tipo == 'empresa':
        return redirect('area_empresa')
    elif perfil.tipo == 'gestor':
        return redirect('area_gestor')
    else:
        return redirect('area_operador')

@login_required(login_url='login')
def area_produtor(request):
    return render(request, 'comerciojusto/area_produtor.html')

@login_required(login_url='login')
def area_empresa(request):
    return render(request, 'comerciojusto/area_empresa.html')

@login_required(login_url='login')
def area_gestor(request):
    return render(request, 'comerciojusto/area_gestor.html')

@login_required(login_url='login')
def area_operador(request):
    return render(request, 'comerciojusto/area_operador.html')
