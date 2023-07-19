from django.urls import path
from contact import views

app_name = 'contatos' 

urlpatterns = [
    path('',views.index, name='home')
]