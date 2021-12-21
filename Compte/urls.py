from django.urls import path

from Compte import views

urlpatterns = [
    path('', views.home, name='accueil'),
    path('Creer_Compte/', views.creerCompte, name='creerCompte'),
]