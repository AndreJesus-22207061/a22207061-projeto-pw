from django.shortcuts import render, redirect
from django.contrib.auth import models, authenticate, login, logout


def registo_view(request):
    if request.method == "POST":
        models.User.objects.create_user(
            username=request.POST['username'],
            email=request.POST['email'],
            first_name=request.POST['nome'],
            last_name=request.POST['apelido'],
            password=request.POST['password']
        )
        return redirect('login')

    return render(request, 'autenticacao/registo.html')


def login_view(request):
    if request.method == "POST":

        # Verifica as credenciais
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            # Se as credenciais são válidas, faz login e redireciona
            login(request, user)
            return render(request, 'autenticacao/user.html')
        else:
            # Se inválidas, reenvia para login com mensagem
            render(request, 'autenticacao/login.html', {
                'mensagem':'Credenciais inválidas'
            })

    return render(request, 'autenticacao/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')