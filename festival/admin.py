from django.contrib import admin
from .models import Localizacao, Banda, Festival



class LocalizacaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cidade', 'pais')
    ordering = ('pais', 'nome', 'cidade')
    search_fields = ('pais', 'nome', 'cidade')


admin.site.register(Localizacao, LocalizacaoAdmin)


class BandaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'genero')
    ordering = ('genero', 'nome')
    search_fields = ('genero','nome')


admin.site.register(Banda, BandaAdmin)



class FestivalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_inicio', 'data_fim', 'localizacao')
    ordering = ('nome', 'localizacao')
    search_fields = ('nome', 'localizacao')
    filter_horizontal = ['bandas']


admin.site.register(Festival, FestivalAdmin)


# Register your models here.
