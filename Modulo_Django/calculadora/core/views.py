from django.shortcuts import render, HttpResponse

# Create your views here.

def calculadora(request, calculo, valorA, valorB ):
    if (calculo == 'soma'):
        resultado = valorA + valorB
        return HttpResponse(f'<h1> SOMA = {valorA} + {valorB} = {resultado} </h1>')
    elif (calculo == 'subtracao'):
        resultado = valorA - valorB
        return HttpResponse(f'<h1> SUBTRAÇÂO = {valorA} - {valorB} = {resultado} </h1>')
    elif (calculo == 'multiplicacao'):
        resultado = valorA * valorB
        return HttpResponse(f'<h1> MULTIPLICAÇÃO = {valorA} * {valorB} = {resultado} </h1>')
    elif (calculo == 'divisao'):
        resultado = valorA / valorB
        return HttpResponse(f'<h1> DIVISÃO = {valorA} / {valorB} = {resultado} </h1>')