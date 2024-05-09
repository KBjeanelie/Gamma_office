# Encodage du fichier
#coding: utf-8

# Importations des modules
from django.contrib import admin
from Paiements.models import *

# Définitions des classes ModelAdmin
@admin.register(Paiements_Demande_Bac)
class Paiements_Demande_BacAdmin(admin.ModelAdmin):

    fieldsets = (("Informations du paiement", {'fields': ('demande', 'montant', 'type_de_paiement',)}),)

    list_display = ('demande', 'montant', 'type_de_paiement', 'date_de_paiement',)

    list_filter = ('date_de_paiement',)

    ordering = ('-date_de_paiement',)

@admin.register(Paiements_Demande_Bepc)
class Paiements_Demande_BepcAdmin(admin.ModelAdmin):

    fieldsets = (("Informations du paiement", {'fields': ('demande', 'montant', 'type_de_paiement',)}),)

    list_display = ('demande', 'montant', 'type_de_paiement', 'date_de_paiement',)

    list_filter = ('date_de_paiement',)

    ordering = ('-date_de_paiement',)

@admin.register(Paiements_Demande_Cepe)
class Paiements_Demande_CepeAdmin(admin.ModelAdmin):

    fieldsets = (("Informations du paiement", {'fields': ('demande', 'montant', 'type_de_paiement',)}),)

    list_display = ('demande', 'montant', 'type_de_paiement', 'date_de_paiement',)

    list_filter = ('date_de_paiement',)

    ordering = ('-date_de_paiement',)