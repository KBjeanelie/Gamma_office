# Encodage du fichier
#coding: utf-8

# Importations des modules
from django.db import models
from Demandes.models import *

# Définitions des classes Models
class Registre_Demande_Bac(models.Model):
    # Docstring de la classe
    """

        Résumé :

            --  Cette classe models intitulée Registre_Demande_Bac représente en base de données la table
            --  Du registre des clients des demandes BAC.

        Attributs :

            --  demande : Représente la demande
            --  nom : Représente le nom
            --  prenoms : Représente le/les prénoms
            --  date_de_naissance : Représente la date de naissance
            --  lieu_de_naissance : Représente le lieu de naissance
            --  domicile : Représente l'adresse de domiciliation
            --  numero_piece : Représente le numéro de la pièce d'identité
            --  date_d_enregistrement : Représente la date d'enregistrement
    
    """

    demande = models.OneToOneField(Demande_Bac, on_delete = models.CASCADE, primary_key = True, null = False, blank = False,verbose_name = "Demande")
    nom = models.CharField(max_length = 50, null = False, blank = False, verbose_name = "Nom")
    prenoms = models.CharField(max_length = 150, null = False, blank = False, verbose_name = "Prénoms")
    date_de_naissance = models.CharField(max_length = 50, null = False, blank = False, verbose_name = "Date de naissance")
    lieu_de_naissance = models.CharField(max_length = 150, null = False, blank = False, verbose_name = "Lieu de naissance")
    domicile = models.CharField(max_length = 150, null = False, blank = False, verbose_name = "Domicile")
    numero_piece = models.CharField(max_length = 150, null = False, blank = False, verbose_name = "Numéro de la pièce d'identité")
    date_d_enregistrement = models.DateTimeField(auto_now_add = True, null = False, blank = False, verbose_name = "Date d'enregistrement")

    # Définition des méthodes et sous classes
    def __str__(self):

        return str(self.date_d_enregistrement)
    
    class Meta:

        verbose_name = 'Registre de demande BAC'
        verbose_name_plural = 'Registre des demandes BAC'

        ordering = ["-date_d_enregistrement"]

class Registre_Demande_Bepc(models.Model):
    # Docstring de la classe
    """

        Résumé :

            --  Cette classe models intitulée Registre_Demande_Bepc représente en base de données la table
            --  Du registre des clients des demandes BEPC.

        Attributs :

            --  demande : Représente la demande
            --  nom : Représente le nom
            --  prenoms : Représente le/les prénoms
            --  date_de_naissance : Représente la date de naissance
            --  lieu_de_naissance : Représente le lieu de naissance
            --  domicile : Représente l'adresse de domiciliation
            --  numero_piece : Représente le numéro de la pièce d'identité
            --  date_d_enregistrement : Représente la date d'enregistrement
    
    """

    demande = models.OneToOneField(Demande_Bepc, on_delete = models.CASCADE, primary_key = True, null = False, blank = False,verbose_name = "Demande")
    nom = models.CharField(max_length = 50, null = False, blank = False, verbose_name = "Nom")
    prenoms = models.CharField(max_length = 150, null = False, blank = False, verbose_name = "Prénoms")
    date_de_naissance = models.CharField(max_length = 50, null = False, blank = False, verbose_name = "Date de naissance")
    lieu_de_naissance = models.CharField(max_length = 150, null = False, blank = False, verbose_name = "Lieu de naissance")
    domicile = models.CharField(max_length = 150, null = False, blank = False, verbose_name = "Domicile")
    numero_piece = models.CharField(max_length = 150, null = False, blank = False, verbose_name = "Numéro de la pièce d'identité")
    date_d_enregistrement = models.DateTimeField(auto_now_add = True, null = False, blank = False, verbose_name = "Date d'enregistrement")

    # Définition des méthodes et sous classes
    def __str__(self):

        return str(self.date_d_enregistrement)
    
    class Meta:

        verbose_name = 'Registre de demande BEPC'
        verbose_name_plural = 'Registre des demandes BEPC'

        ordering = ["-date_d_enregistrement"]

class Registre_Demande_Cepe(models.Model):
    # Docstring de la classe
    """

        Résumé :

            --  Cette classe models intitulée Registre_Demande_Cepe représente en base de données la table
            --  Du registre des clients des demandes CEPE.

        Attributs :

            --  demande : Représente la demande
            --  nom : Représente le nom
            --  prenoms : Représente le/les prénoms
            --  date_de_naissance : Représente la date de naissance
            --  lieu_de_naissance : Représente le lieu de naissance
            --  domicile : Représente l'adresse de domiciliation
            --  numero_piece : Représente le numéro de la pièce d'identité
            --  date_d_enregistrement : Représente la date d'enregistrement
    
    """

    demande = models.OneToOneField(Demande_Cepe, on_delete = models.CASCADE, primary_key = True, null = False, blank = False,verbose_name = "Demande")
    nom = models.CharField(max_length = 50, null = False, blank = False, verbose_name = "Nom")
    prenoms = models.CharField(max_length = 150, null = False, blank = False, verbose_name = "Prénoms")
    date_de_naissance = models.CharField(max_length = 50, null = False, blank = False, verbose_name = "Date de naissance")
    lieu_de_naissance = models.CharField(max_length = 150, null = False, blank = False, verbose_name = "Lieu de naissance")
    domicile = models.CharField(max_length = 150, null = False, blank = False, verbose_name = "Domicile")
    numero_piece = models.CharField(max_length = 150, null = False, blank = False, verbose_name = "Numéro de la pièce d'identité")
    date_d_enregistrement = models.DateTimeField(auto_now_add = True, null = False, blank = False, verbose_name = "Date d'enregistrement")

    # Définition des méthodes et sous classes
    def __str__(self):

        return str(self.date_d_enregistrement)
    
    class Meta:

        verbose_name = 'Registre de demande CEPE'
        verbose_name_plural = 'Registre des demandes CEPE'

        ordering = ["-date_d_enregistrement"]