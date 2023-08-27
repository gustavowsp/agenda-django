from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
from contact.forms import ContactForm
from contact import models




def create(request):
  
  form_ction = reverse('contatos:create')

  if request.method == 'POST':
    # Criando um novo formulário com as informações enviadas
    form = ContactForm(request.POST,request.FILES)

    context = {
      'form' : form,
      'form_action' : form_ction,
      'acao_nome_post' : 'Cadastrar novo contato'
    }
    
    # Aparentemente para chamar o método clean, tenho que chamar o is_valid()
    if form.is_valid():

      # Pegando o contato recém salvo
      contact = form.save()
      
      # Retornand o id do contato para update
      return redirect('contatos:update', id_contact=contact.id)
    
    return render(
      request, 
      'contact/create.html', 
      context
    ) 

  # Quando o usuário acessar essa view via get 
  # vamos enviar o formulário vazio no context para o preenchimento.
  context = {
    'form' : ContactForm(),
    'form_action' : form_ction,
    'acao_nome_post' : 'Cadastrar novo contato'
  }

  return render(
      request, 
      'contact/create.html', 
      context
    )

def update(request,id_contact):
  
  # Criando o action do form, para que os dados enviados venham à essa view
  form_action_url = reverse('contatos:update', args=(id_contact,))

  context = {
    'form_action' : form_action_url,
    'acao_nome_post' : 'Atualizar dados'
  }
  # Buscando o objeto requisitado ou retornando um erro 404
  contato_objeto = get_object_or_404(
    models.Contact,
    show = True,
    id = id_contact
    )


  # Caso o usuário queira atualizar o contato, entra em post, caso não, vamos 
  # apenas exibir os dados do objeto para iniciar a alteração.
  if request.method == 'POST':

    # Criando um formulário com novos dados enviados pelo usuário
    formulario = ContactForm(
      data=request.POST,
      files=request.FILES,
      instance=contato_objeto
    )

    if formulario.is_valid():
      registro = formulario.save()
      return redirect('contatos:single_contact', registro.id)

  else:

    # Passando o objeto para o formulário, assim resultando em apenas alterações
    formulario = ContactForm(instance=contato_objeto)


  context['form'] = formulario

  return render(
    request,
    'contact/create.html',
    context
    )

def delete(request,id_contact):

  # Criando o form action
  form_action = reverse('contatos:delete_contact', args=(id_contact,))


  # Recuperando contato para operação de delete
  contato = get_object_or_404(models.Contact, id=id_contact)

  # Buscando confirmação para delete
  deletar = request.POST.get('confirmacao','nao')
 
  context = {
    'form_action' : form_action,
    'contact' : contato,
    'confirmacao' : deletar
  }


  if deletar == 'sim':
    contato.delete()
    return redirect("contatos:home")
  
  return render(
    request,
    'contact/unico_contato.html',
    context
  )
