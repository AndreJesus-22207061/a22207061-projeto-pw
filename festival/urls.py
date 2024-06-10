from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_festivais, name='lista_festivais'),
    path('festivais/<int:festival_id>/', views.detalhes_festival, name='detalhes_festival'),
]