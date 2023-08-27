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
    
    # User - CRUD
    #path('user/<int:id_user>/detail/',views.contact, name='usuario'), # R
    path('user/create/',views.create_user, name='create_user'), # C
    #path('user/<int:id_user>/update',views.update, name='update_user'), # U
    #path('user/<int:id_user>/delete',views.delete, name='delete_user'),
]