import logging
from django.shortcuts import render
from .models import Usuario
from django.http import HttpResponse

# Create a logger
logger = logging.getLogger(__name__)

def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')

        # Debugging: print form data
        logger.debug(f"Received data - Nome: {nome}, Idade: {idade}")

        # Ensure both nome and idade are provided
        if nome and idade:
            try:
                novo_usuario = Usuario(nome=nome, idade=int(idade))
                novo_usuario.save()
                logger.debug(f"User {nome} saved successfully.")
            except Exception as e:
                logger.error(f"Error saving user: {e}")
                return HttpResponse(f"Error saving user: {e}", status=500)
        else:
            logger.warning("Nome or idade not provided.")
            return HttpResponse("Nome or idade not provided.", status=400)

    # Retrieve all users
    try:
        usuarios = {"usuarios": Usuario.objects.all()}
        logger.debug(f"Retrieved users: {usuarios}")
    except Exception as e:
        logger.error(f"Error retrieving users: {e}")
        return HttpResponse(f"Error retrieving users: {e}", status=500)

    try:
        return render(request, 'usuarios/usuarios.html', usuarios)
    except Exception as e:
        logger.error(f"Error rendering template: {e}")
        return HttpResponse(f"Error rendering template: {e}", status=500)