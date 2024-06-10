from django.urls import path
from . import views

app_name = "bandas"

urlpatterns = [
    path('', views._bandas_view, name='lista_bandas'),
    path('banda/<int:banda_id>/', views._banda_view, name='banda'),
    path('album/<int:album_id>/', views._album_view, name='album'),
    path('musica/<int:musica_id>/', views._musica_view, name='musica'),
    path('banda/nova/', views.nova_banda_view, name='nova_banda'),
    path('banda/<int:banda_id>/novo_album/', views.novo_album, name='novo_album'),
    path('album/<int:album_id>/nova_musica/', views.nova_musica, name='nova_musica'),
    path('banda/<int:banda_id>/confirm_delete/', views.confirm_delete_banda, name='confirm_delete_banda'),
    path('album/<int:album_id>/confirm_delete/', views.confirm_delete_album, name='confirm_delete_album'),
    path('musica/<int:musica_id>/confirm_delete/', views.confirm_delete_musica, name='confirm_delete_musica'),
    path('banda/<int:banda_id>/editar/', views.editar_banda, name='editar_banda'),
    path('album/<int:album_id>/editar/', views.editar_album, name='editar_album'),
    path('musica/<int:musica_id>/editar/', views.editar_musica, name='editar_musica'),
    path('html-css/', views.html_css_view, name='html_css_view'),
]