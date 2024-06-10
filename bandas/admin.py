from django.contrib import admin
from django.utils.html import format_html
from .models import Banda
from .models import Album
from .models import Musica

class AlbumInLine(admin.TabularInline):
    model = Album


class BandaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'genero')
    ordering = ('genero', 'nome')
    search_fields = ('genero','nome')
    inlines = [AlbumInLine]



admin.site.register(Banda, BandaAdmin)




class MusicaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tempo', 'spotify_link')
    ordering = ('tempo', 'nome')
    search_fields = ['nome']



admin.site.register(Musica, MusicaAdmin)




class AlbumAdmin(admin.ModelAdmin):
    list_display = ('nome', 'banda', 'ano_lancamento')
    ordering = ('banda', 'nome', 'ano_lancamento')
    search_fields = ('banda','nome', 'ano_lancamento')
    filter_horizontal = ('musicas',)






admin.site.register(Album, AlbumAdmin)


