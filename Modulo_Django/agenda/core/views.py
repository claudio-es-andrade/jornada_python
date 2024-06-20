from django.contrib.auth.models import User
from django.shortcuts import render, redirect, HttpResponse

from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import datetime, timedelta
from django.http.response import Http404, JsonResponse


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
    usuario    = request.user
    data_atual = datetime.now() - timedelta(hours=1)   # Trazer eventos da data atual em diante e apagar os eventos antigos
    evento     = Evento.objects.filter(usuario=usuario, data_evento__gt=data_atual)     #Evento.objects.filter(usuario=usuario)  #Evento.objects.get(id = 1)
    dados      = {'eventos' : evento}
    return render(request, 'agenda.html', dados)
def index(request):
    return redirect('/agenda/')

@login_required(login_url='/login/')
def evento(request):
    id_evento = request.GET.get('id')
    dados = {}
    if id_evento:
        dados['evento'] = Evento.objects.get(id=id_evento)
    return render(request, 'evento.html', dados)

@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        titulo          = request.POST.get('titulo')
        local           = request.POST.get('local')
        data_evento     = request.POST.get('data_evento')
        descricao       = request.POST.get('descricao')
        usuario         = request.user
        id_evento       = request.POST.get('id_evento')
        if id_evento:
            evento = Evento.objects.get(id=id_evento)
            if evento.usuario == usuario:
                evento.titulo      = titulo
                evento.local       = local
                evento.descricao   = descricao
                evento.data_evento = data_evento
                evento.save()
            # Evento.objects.filter(id=id_evento).update(titulo=titulo,
            #                       local=local,
            #                       data_evento=data_evento,
            #                       descricao=descricao,
            #                       usuario=usuario)
        else:
            Evento.objects.create(titulo=titulo,
                                    local=local,
                                    data_evento=data_evento,
                                    descricao=descricao,
                                    usuario=usuario)
    return redirect('/')

@login_required(login_url='/login/')
def delete_evento(request, id_evento):
    usuario = request.user
    try:
        evento  = Evento.objects.get(id=id_evento)
    except Exception:
        raise Http404
    if usuario == evento.usuario:
        evento.delete()
    else:
        raise Http404()
    return redirect('/')

#@login_required(login_url='/login/')
def json_lista_evento(request, id_usuario):
    usuario = User.objects.get(id=id_usuario)    #request.user
    evento = Evento.objects.filter(usuario=usuario).values('id', 'titulo')

    return JsonResponse(list(evento), safe=False)