from django.urls import path
from . import views


app_name = "meteo"
urlpatterns = [
    path('tempoLisboa/', views.tempo_lisboa , name='tempo_lisboa'),
    path('previsao5Dias/', views.previsao_proximos_5dias, name='previsao_proximos_5dias'),
    path('api/cidades', views.listar_cidades , name='cidadesAPI'),
    path('api/previsao_hoje/<int:cidade_id>/', views.previsao_hojeAPI , name='previsao_hojeAPI'),
    path('api/previsao_proximos_5dias/<int:cidade_id>/', views.previsao_proximos_5diasAPI , name='previsao_proximos_5diasAPI'),
    path('explicaAPI/', views.explicaAPI , name='explicaAPI'),
]