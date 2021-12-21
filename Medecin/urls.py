from django.urls import path

from Medecin import views

urlpatterns = [
    path('', views.home),
    path('Modifier_Compte/', views.modifierCompte),
    path('RendezVous_Annuler/', views.rendezVousAnnuler),
]