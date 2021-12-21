from django.urls import path

from Pharmacien import views

urlpatterns = [
    path('', views.home),
    path('modifier_compte/', views.modifierCompte),
    path('gerer_medicament/', views.gererMedicament),

]