from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.index, name='index'),
    path('contacts', views.contacts, name='contacts'),
    path('aboutme', views.aboutme, name='aboutme'),
    path('sobrepw', views.sobrepw, name = 'sobrepw'),
]