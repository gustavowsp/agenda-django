from django.db import models
from django.utils import timezone

# Create your models here.
class Contact(models.Model):
  primeiro_nome = models.CharField(max_length=255)
  ultimo_nome   = models.CharField(max_length=255)
  telefone      = models.CharField(max_length=255)
  email         = models.EmailField(max_length=255,blank=True)
  data_criacao  = models.DateTimeField(default=timezone.now)
  descricao     = models.TextField(blank=True)

  def __str__(self) -> str:
    return f'{self.primeiro_nome} {self.ultimo_nome}'
