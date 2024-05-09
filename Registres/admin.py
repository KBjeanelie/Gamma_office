# Encodage du fichier
#coding: utf-8

# Importations des modules
from django.contrib import admin
from Registres.models import *

# Définitions des classes ModelAdmin
@admin.register(Registre_Demande_Bac)
class Registre_Demande_BacAdmin(admin.ModelAdmin):

    fieldsets = (("Informations du registre", {'fields': ('demande', 'nom', 'prenoms', 'date_de_naissance', 'lieu_de_naissance', 'domicile', 'numero_piece',)}),)

    list_display = ('demande', 'nom', 'prenoms', 'date_de_naissance', 'date_d_enregistrement',)

    list_filter = ('date_d_enregistrement',)

    ordering = ('-date_d_enregistrement',)

@admin.register(Registre_Demande_Bepc)
class Registre_Demande_BepcAdmin(admin.ModelAdmin):

    fieldsets = (("Informations du registre", {'fields': ('demande', 'nom', 'prenoms', 'date_de_naissance', 'lieu_de_naissance', 'domicile', 'numero_piece',)}),)

    list_display = ('demande', 'nom', 'prenoms', 'date_de_naissance', 'date_d_enregistrement',)

    list_filter = ('date_d_enregistrement',)

    ordering = ('-date_d_enregistrement',)

@admin.register(Registre_Demande_Cepe)
class Registre_Demande_CepeAdmin(admin.ModelAdmin):

    fieldsets = (("Informations du registre", {'fields': ('demande', 'nom', 'prenoms', 'date_de_naissance', 'lieu_de_naissance', 'domicile', 'numero_piece',)}),)

    list_display = ('demande', 'nom', 'prenoms', 'date_de_naissance', 'date_d_enregistrement',)

    list_filter = ('date_d_enregistrement',)

    ordering = ('-date_d_enregistrement',)