# Encodage du fichier
#coding: utf-8

# Importations des modules
from django.urls import path
from API.views.auth import GetAllStatusView
from Demandes.views import *

# Définitions des urls de l'application
urlpatterns = [
    path('all-status/', view=GetAllStatusView.as_view(), name='all-status')
]