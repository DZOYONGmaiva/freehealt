from django.urls import path

from Patient import views

urlpatterns = [
    path('', views.home),
    path('inscription/', views.inscription),
   # path('supprimer_comptecc', views.creeObjectCC, name='supprimer'),

    path('modifier_compte', views.modifierCompte),
    path('prendre_rdv', views.prendreRendezVous),
    path('annuler_rdv', views.modifierAnnulerRendezVous),

]