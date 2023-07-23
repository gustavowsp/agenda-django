from django.db import models
from django.utils import timezone

# Create your models here.

class Category(models.Model):
  name = models.CharField(max_length=55)

class Contact(models.Model):
  primeiro_nome = models.CharField(max_length=255)
  ultimo_nome   = models.CharField(max_length=255)
  telefone      = models.CharField(max_length=255)
  email         = models.EmailField(max_length=255,blank=True)
  data_criacao  = models.DateTimeField(default=timezone.now)
  descricao     = models.TextField(blank=True)
  show          = models.BooleanField(default=True)
  picture       = models.ImageField(blank=True, upload_to=r'pictures/%Y/%m/%d')
  
  #category      = models.ForeignKey(Category, on_delete=models.CASCADE)
  # category      = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
  category      = models.ForeignKey(
    Category, 
    on_delete=models.SET_NULL,
    blank=True, null=True
    )

  def __str__(self) -> str:
    return f'{self.primeiro_nome} {self.ultimo_nome}'
