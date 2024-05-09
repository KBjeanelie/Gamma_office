# Encodage du fichier
#coding: utf-8

# Importations des modules
from django.contrib import admin
from Profils.models import *

# Définitions des classes ModelAdmin
@admin.register(Agent_De_Reception)
class Agent_De_ReceptionAdmin(admin.ModelAdmin):

    fieldsets = (('Informations du profil', {'fields': ('nom', 'prenoms', 'photo_de_profil',)}),('Compte utilisateur', {'fields': ('compte_agent_de_reception',)}),)

    list_display = ('nom', 'prenoms', 'compte_agent_de_reception',)

    list_filter = ('date_de_creation',)

    ordering = ('-date_de_creation',)

@admin.register(Agent_Regisseur)
class Agent_RegisseurAdmin(admin.ModelAdmin):

    fieldsets = (('Informations du profil', {'fields': ('nom', 'prenoms', 'photo_de_profil',)}),('Compte utilisateur', {'fields': ('compte_agent_regisseur',)}),)

    list_display = ('nom', 'prenoms', 'compte_agent_regisseur',)

    list_filter = ('date_de_creation',)

    ordering = ('-date_de_creation',)

@admin.register(Agent_Charge_De_Diplome)
class Agent_Charge_De_DiplomeAdmin(admin.ModelAdmin):

    fieldsets = (('Informations du profil', {'fields': ('nom', 'prenoms', 'photo_de_profil',)}),('Compte utilisateur', {'fields': ('compte_agent_charge_de_diplome',)}),)

    list_display = ('nom', 'prenoms', 'compte_agent_charge_de_diplome',)

    list_filter = ('date_de_creation',)

    ordering = ('-date_de_creation',)

@admin.register(Agent_De_Verification)
class Agent_De_VerificationAdmin(admin.ModelAdmin):

    fieldsets = (('Informations du profil', {'fields': ('nom', 'prenoms', 'photo_de_profil',)}),('Compte utilisateur', {'fields': ('compte_agent_de_verification',)}),)

    list_display = ('nom', 'prenoms', 'compte_agent_de_verification',)

    list_filter = ('date_de_creation',)

    ordering = ('-date_de_creation',)

@admin.register(Agent_De_Production)
class Agent_De_ProductionAdmin(admin.ModelAdmin):

    fieldsets = (('Informations du profil', {'fields': ('nom', 'prenoms', 'photo_de_profil',)}),('Compte utilisateur', {'fields': ('compte_agent_de_production',)}),)

    list_display = ('nom', 'prenoms', 'compte_agent_de_production',)

    list_filter = ('date_de_creation',)

    ordering = ('-date_de_creation',)

@admin.register(Agent_De_Distribution)
class Agent_De_DistributionAdmin(admin.ModelAdmin):

    fieldsets = (('Informations du profil', {'fields': ('nom', 'prenoms', 'photo_de_profil',)}),('Compte utilisateur', {'fields': ('compte_agent_de_distribution',)}),)

    list_display = ('nom', 'prenoms', 'compte_agent_de_distribution',)

    list_filter = ('date_de_creation',)

    ordering = ('-date_de_creation',)
