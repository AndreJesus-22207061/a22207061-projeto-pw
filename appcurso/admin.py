from django.contrib import admin
from .models import Disciplina, LinguagemDeProgramacao, Docente, AreaCientifica, Projeto, Curso

class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ano', 'semestre', 'ects')
    ordering = ('nome', 'ano', 'semestre', 'ects')
    search_fields = ('nome', 'ano', 'semestre')

admin.site.register(Disciplina, DisciplinaAdmin)

class LinguagemDeProgramacaoAdmin(admin.ModelAdmin):
    list_display = ('nome',)  # Use uma vírgula para criar uma tupla com um único elemento
    search_fields = ('nome',)

admin.site.register(LinguagemDeProgramacao, LinguagemDeProgramacaoAdmin)

class DocenteAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

admin.site.register(Docente, DocenteAdmin)

class AreaCientificaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

admin.site.register(AreaCientifica, AreaCientificaAdmin)

class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'disciplina')  # Remova 'linguagens' pois não é possível exibir um campo ManyToManyField diretamente
    ordering = ('nome', 'disciplina')
    search_fields = ('nome',)

admin.site.register(Projeto, ProjetoAdmin)

class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

admin.site.register(Curso, CursoAdmin)

# Register your models here.
