# Encodage du fichier
#coding: utf-8

# Importations des modules
from django.contrib import admin
from Demandes.models import *

# Définitions des classes ModelAdmin
@admin.register(Demande_Bac)
class Demande_BacAdmin(admin.ModelAdmin):

    fieldsets = (('Informations de la demande BAC', {'fields': ('objet', 'matricule', 'nom', 'prenoms', 'date_de_naissance', 'lieu_de_naissance', 'numero_de_telephone', 'departement', 'etablissement_d_origine', 'annee_d_obtention_du_bac', 'copie_couleur_de_l_acte_de_naissance', 'copie_couleur_du_bepc', 'copie_couleur_d_une_piece_d_identite',)}),)

    list_display = ('objet', 'matricule', 'nom', 'prenoms', 'date_d_enregistrement',)

    list_filter = ('date_d_enregistrement',)

    ordering = ('-date_d_enregistrement',)

@admin.register(Activites_Demande_Bac)
class Activites_Demande_BacAdmin(admin.ModelAdmin):

    fieldsets = (("Informations de l'activité", {'fields': ('demande', 'utilisateur', 'type_de_traitement',)}),)

    list_display = ('demande', 'utilisateur', 'type_de_traitement', 'date_de_traitement',)

    list_filter = ('date_de_traitement',)

    ordering = ('-date_de_traitement',)

@admin.register(Demande_Bepc)
class Demande_BepcAdmin(admin.ModelAdmin):

    fieldsets = (('Informations de la demande BEPC', {'fields': ('objet', 'matricule', 'nom', 'prenoms', 'date_de_naissance', 'lieu_de_naissance', 'numero_de_telephone', 'departement', 'etablissement_d_origine', 'annee_d_obtention_du_bepc', 'copie_couleur_de_l_acte_de_naissance', 'copie_couleur_du_cepe', 'copie_couleur_d_une_piece_d_identite',)}),)

    list_display = ('objet', 'matricule', 'nom', 'prenoms', 'date_d_enregistrement',)

    list_filter = ('date_d_enregistrement',)

    ordering = ('-date_d_enregistrement',)

@admin.register(Activites_Demande_Bepc)
class Activites_Demande_BepcAdmin(admin.ModelAdmin):

    fieldsets = (("Informations de l'activité", {'fields': ('demande', 'utilisateur', 'type_de_traitement',)}),)

    list_display = ('demande', 'utilisateur', 'type_de_traitement', 'date_de_traitement',)

    list_filter = ('date_de_traitement',)

    ordering = ('-date_de_traitement',)

@admin.register(Demande_Cepe)
class Demande_CepeAdmin(admin.ModelAdmin):

    fieldsets = (('Informations de la demande CEPE', {'fields': ('objet', 'matricule', 'nom', 'prenoms', 'date_de_naissance', 'lieu_de_naissance', 'numero_de_telephone', 'departement', 'etablissement_d_origine', 'annee_d_obtention_du_cepe', 'copie_couleur_de_l_acte_de_naissance', 'copie_couleur_d_une_piece_d_identite',)}),)

    list_display = ('objet', 'matricule', 'nom', 'prenoms', 'date_d_enregistrement',)

    list_filter = ('date_d_enregistrement',)

    ordering = ('-date_d_enregistrement',)

@admin.register(Activites_Demande_Cepe)
class Activites_Demande_CepeAdmin(admin.ModelAdmin):

    fieldsets = (("Informations de l'activité", {'fields': ('demande', 'utilisateur', 'type_de_traitement',)}),)

    list_display = ('demande', 'utilisateur', 'type_de_traitement', 'date_de_traitement',)

    list_filter = ('date_de_traitement',)

    ordering = ('-date_de_traitement',)