from django.urls import path
from . import views


app_name="appcurso"

urlpatterns = [
    path('', views.curso_view, name='curso'),
    path('disciplinas/', views.disciplinas_view, name='lista_disciplinas'),
    path('disciplina/<int:disciplina_id>/', views.disciplina_view, name='disciplina'),
    path('projeto/<int:projeto_id>/', views.projeto_view, name='projeto'),
    path('adicionar-disciplina/', views.adicionar_disciplina, name='adicionar_disciplina'),
    path('adicionar-projeto/<int:disciplina_id>/', views.adicionar_projeto, name='adicionar_projeto'),
    path('editar-disciplina/<int:disciplina_id>/', views.editar_disciplina, name='editar_disciplina'),
    path('editar-projeto/<int:projeto_id>/', views.editar_projeto, name='editar_projeto'),
    path('projetos/', views.lista_projetos, name='lista_projetos'),
    path('adicionar_lista_projeto/', views.add_lista_projetos, name='adicionar_lista_projeto'),
]