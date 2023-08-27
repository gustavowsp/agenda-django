from typing import Any, Dict
from django import forms
from django.core.exceptions import ValidationError
from contact.models import Contact


class ContactForm(forms.ModelForm):
    
    # teste = forms.CharField(
    #   max_length=50,
    #   widget=forms.TextInput(
    #     attrs={
    #       'placeholder' : 'Digite o que você achou do nosso sistema de cadastro',
    #       'class' : 'form-control'
    #     }
    #   ),
    #   label='Comentário',
    #   help_text='Digite até cinquenta caracteres...',
        
    # )
    
    class Meta:
      model = Contact
      fields = ('picture','primeiro_nome','ultimo_nome','telefone','category','email')

      # widgets = {
      #   'telefone' : forms.NumberInput(
      #     attrs = {
      #       'placeholder' : 'Telefone: 11940518455'
      #     }
      #   )
      # }
  

    def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)

      self.fields['primeiro_nome'].widget.attrs.update(
        {
          'placeholder' : 'Seu primeiro nome'
        }
      )
      self.fields['ultimo_nome'].widget.attrs.update(
        {
          'placeholder' : 'Seu último nome'
        }
      )
      self.fields['telefone'].widget.attrs.update(
        {
          'placeholder' : 'Seu telefone'
        }
      )
      self.fields['email'].widget.attrs.update(
        {
          'placeholder' : 'example@com.br'
        }
      )

    def clean(self):

      clenead_data = self.cleaned_data

      primeiro_nome = clenead_data.get('primeiro_nome')
      ultimo_nome = clenead_data.get('ultimo_nome')

      if primeiro_nome == ultimo_nome:
        msg = ValidationError(
          'O primeiro e último nome devem ser diferentes!',
          code='invalid'
          )
        
        self.add_error('primeiro_nome',msg)
        self.add_error('ultimo_nome',msg)
        self.add_error(None,msg)

      return super().clean()

    def clean_telefone(self):
      
      telefone = self.cleaned_data.get('telefone')
     
      # Checando se telefone possui 11 caracteres
      if len(telefone) != 11:
        self.add_error(
          'telefone',
          ValidationError(
            'O telefone deve possuir onze caracteres.',
            code='invalid'
          )
        )

      return telefone

    def clean_primeiro_nome(self):
      
      # Recuperando o primeiro nome
      primeiro_nome = self.cleaned_data.get('primeiro_nome')
      
      # Checando se foi enviado primeiro nome
      if not primeiro_nome:
         self.add_error(
          'primeiro_nome',
          ValidationError(
              'Você deve enviar o primeiro nome',
              code='invalid'
            )
          )

      # Checando tamanho do primeiro nome
      if len(primeiro_nome) < 2:
         self.add_error(
          'primeiro_nome',
          ValidationError(
            'O primero nome deve possuir mais de 2 caracteres!',
            code='invalid'
          )
         )

      # Checa se usuário realmente só enviou um nome
      if len(primeiro_nome.split()) > 1:
        self.add_error(
          'primeiro_nome',
          ValidationError(
            'Usuário, você apenas pode digitar um nome no primeiro nome!',
            code='invalid'
           )
        )

      return primeiro_nome
    