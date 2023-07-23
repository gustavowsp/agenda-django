from django.contrib import admin
from contact import models


# Register your models here.
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','primeiro_nome','ultimo_nome','data_criacao']
    list_display_links = ['id','primeiro_nome']
    ordering = ['-id']
    search_fields = ['primeiro_nome','ultimo_nome']
    list_filter = ['data_criacao','id']
    #list_editable = ['ultimo_nome']
    list_per_page = 1
    list_max_show_all = 10
