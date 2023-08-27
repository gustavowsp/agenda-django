from django.urls import path
from contact import views

app_name = 'contatos' 

urlpatterns = [
    path('',views.index, name='home'),
    path('search/',views.search, name='search'),

    # Contacts - CRUD
    path('contact/<int:id_contact>/detail/',views.contact, name='single_contact'), # R
    path('contact/create/',views.create, name='create'), # C
    path('contact/<int:id_contact>/update',views.update, name='update'), # U
    path('contact/<int:id_contact>/delete',views.delete, name='delete_contact'),
]