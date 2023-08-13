from django.shortcuts import render

# Create your views here.
def index(request):
    
    context = {
        'titulo' : 'Contatos'
    }
    return render(
      request,
      'contact/index.html',
      context)