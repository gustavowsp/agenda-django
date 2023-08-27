from django.shortcuts import render, redirect,get_object_or_404
from django.db.models import Q
from contact.models import Contact
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    
    contatos = Contact.objects.filter(show=True).order_by('-id')
    contatos_paginacao = Paginator(contatos,10)
    
    number_page = request.GET.get('page',1)
    pagina_do_contato = contatos_paginacao.get_page(number_page)
    context = {
        'titulo' : 'Contatos',
        'contatos' : pagina_do_contato
    }

    return render(
      request,
      'contact/index.html',
      context
      )

def contact(request,id_contact):

    single_contact = get_object_or_404(
        Contact, 
        id=id_contact, show=True
        )

    context = {
        'contact' : single_contact
    }

    return render(request,'contact/unico_contato.html',context)

def search(request):

    search_value = request.GET.get('q','').strip()
    
    if not search_value:
        return redirect('contatos:home')


    contatos = Contact.objects.filter \
        (
            show=True
        ).filter \
        (
            Q(primeiro_nome__icontains=search_value)|
            Q(ultimo_nome__icontains=search_value) |
            Q(telefone__icontains=search_value) |
            Q(email__icontains=search_value)
        )
    
    # Criando uma paginação
    contatos_paginator = Paginator(contatos,10)

    page_number = request.GET.get('page',1)
    pagina_contato = contatos_paginator.page(page_number)
    
    context = {
        'titulo' : 'Contatos',
        'contatos' : pagina_contato,
    }

    return render(
      request,
      'contact/index.html',
      context)

