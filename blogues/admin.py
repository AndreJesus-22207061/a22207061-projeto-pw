from django.contrib import admin
from .models import Artigo
from .models import Categoria
from .models import Comentario
from .models import Rating
from .models import Autor


class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome','idade','email')
    ordering = ('nome','idade')
    search_fields = ('nome','idade','email')

admin.site.register(Autor, AutorAdmin)

class ArtigoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'data_publicacao')
    ordering = ('titulo', 'autor', 'data_publicacao')
    search_fields = ('titulo', 'autor', 'data_publicacao')

admin.site.register(Artigo, ArtigoAdmin)

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('autor', 'artigo', 'data_publicacao', 'texto')
    ordering = ('autor', 'artigo', 'data_publicacao')
    search_fields = ('autor', 'artigo', 'data_publicacao')

admin.site.register(Comentario, ComentarioAdmin)


class CategoriaInLine(admin.TabularInline):
    model=Categoria

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome']
    ordering = ['nome']
    search_fields = ['nome']
    filter_horizontal = ('artigos',)


admin.site.register(Categoria, CategoriaAdmin)

class RatingAdmin(admin.ModelAdmin):
    list_display = ('artigo','autor','rating')
    ordering = ['rating']
    search_fields = ('artigo', 'rating')

admin.site.register(Rating, RatingAdmin)

