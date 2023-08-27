from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
  
  class Meta:
    verbose_name = 'Categoria'
    verbose_name_plural = 'Categorias'

  name = models.CharField(max_length=55)

  def __str__(self) -> str:
    return self.name

class Contact(models.Model):

  class Meta:
    verbose_name = 'Contato'
    verbose_name_plural = 'Contatos'

  primeiro_nome = models.CharField(max_length=255, blank=True)
  ultimo_nome   = models.CharField(max_length=255, blank=True)
  telefone      = models.CharField(max_length=255, blank=True)
  email         = models.EmailField(max_length=255,blank=True)
  data_criacao  = models.DateTimeField(default=timezone.now, blank=True)
  descricao     = models.TextField(blank=True)
  show          = models.BooleanField(default=True, blank=True)
  picture       = models.ImageField(blank=True, upload_to=r'pictures/%Y/%m/%d')
  
  #category     = models.ForeignKey(Category, on_delete=models.CASCADE)
  #category     = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
  category      = models.ForeignKey(
    Category, 
    on_delete=models.SET_NULL,
    blank=True, null=True
    )
  owner         = models.ForeignKey(
    User,
    on_delete= models.SET_NULL,
    null=True, blank=True
    ) 

  def __str__(self) -> str:
    return f'{self.primeiro_nome} {self.ultimo_nome}'
