from django.contrib import admin
from django.utils.html import format_html
from .models import Pessoa




class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'idade')
    ordering = ('idade', 'nome')
    search_fields = ('nome', 'idade')




admin.site.register(Pessoa, PessoaAdmin)

# Register your models here.
