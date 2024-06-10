from django.urls import path
from . import views

app_name = "blogues"

urlpatterns = [
    path('', views.artigos, name='artigos'),
    path('artigo/<int:id>/', views.artigo, name='artigo'),
    path('autores/', views.autores, name='autores'),
    path('autor/<int:id>/', views.autor, name='autor'),
    path('criar_artigo/', views.criar_artigo, name='criar_artigo'),
    path('criar_autor/', views.criar_autor, name='criar_autor'),
    path('artigo/<int:artigo_id>/confirm_delete/', views.confirm_delete_artigo, name='confirm_delete_artigo'),
    path('autor/<int:autor_id>/confirm_delete/', views.confirm_delete_autor, name='confirm_delete_autor'),
    path('artigo/<int:artigo_id>/editar/', views.editar_artigo, name='editar_artigo'),
    path('autor/<int:autor_id>/editar/', views.editar_autor, name='editar_autor'),
]