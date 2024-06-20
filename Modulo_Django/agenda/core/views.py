from django.shortcuts import render, redirect, HttpResponse

from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

# def localTitulo(request, titulo_evento ):
#     resultado = Evento.objects.get(titulo=titulo_evento)
#     if (resultado in Evento):
#         return HttpResponse(f'<h1> LOCAL DO EVENTO: {Evento.local} </h1>')

def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario  = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuário ou senha inválidos")
    return redirect('/')

@login_required(login_url='/login/')
def lista_eventos(request):
    usuario   = request.user
    evento    = Evento.objects.filter(usuario=usuario)     #Evento.objects.filter(usuario=usuario)  #Evento.objects.get(id = 1)
    dados     = {'eventos' : evento}
    return render(request, 'agenda.html', dados)
def index(request):
    return redirect('/agenda/')

@login_required(login_url='/login/')
def evento(request):
    return render(request, 'evento.html')

@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        titulo          = request.POST.get('titulo')
        local           = request.POST.get('local')
        data_evento     = request.POST.get('data_evento')
        descricao       = request.POST.get('descricao')
        usuario         = request.user
        Evento.objects.create(titulo=titulo,
                              local=local,
                              data_evento=data_evento,
                              descricao=descricao,
                              usuario=usuario)
    return redirect('/')