from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse(f'<h1>Olá {nome} de {idade} anos de idade, olá mundo!</h1>')
