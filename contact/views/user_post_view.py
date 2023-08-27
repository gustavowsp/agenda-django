from django.shortcuts import render
from django.urls import reverse
from contact.forms import RegistroUsers
from django.http import HttpResponse

def create_user(request):

    form_action = reverse('contatos:create_user')
    context = {
        'form_action' : form_action,
        'acao_nome_post' : 'Criar conta'
    }

    if request.method == 'POST':
        
        formulario =  RegistroUsers(request.POST)

        # Salvando o novo usuário
        if formulario.is_valid():
            formulario.save()
            return HttpResponse('Usuário criado')
        
        context['form'] = formulario

    else:
        context['form'] = RegistroUsers()
    
    return render(
        request,
        'contact/create.html',
        context
    )


