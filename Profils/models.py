# Encodage du fichier
#coding: utf-8

# Importations des modules
from django.db import models
from Compte.models import Utilisateur
from django.core.validators import FileExtensionValidator

# Définitions des classes Models
class Agent_De_Reception(models.Model):
    # Docstring de la classe
    """

        Résumé :

            --  Cette classe models intitulée Agent_De_Reception représente en base de données la table des
            --  Profils des agents de réception du système.

        Attributs :

            --  nom : Représente le nom du profil de l'agent de réception
            --  prenoms : Représente le/les prénoms de l'agent de réception
            --  photo_de_profil : Représente la photo de profil de l'agent de réception
            --  compte_agent_de_reception : Représente le compte rattaché au profil de l'agent de réception
            --  date_de_creation : Représente la date de création du profil de l'agent de réception

    """

    nom = models.CharField(max_length = 50, null = False, blank = False, verbose_name = "Nom de l'agent de réception")
    prenoms = models.CharField(max_length = 150, null = False, blank = False, verbose_name = "Prénom (s) de l'agent de réception")
    photo_de_profil = models.ImageField(upload_to = "photos_de_profils_agents_de_receptions/", null = False, blank = False, validators = [FileExtensionValidator(allowed_extensions = ["jpg", "png", "jpeg",])], verbose_name = "Photo de profil de l'agent de réception")
    compte_agent_de_reception = models.OneToOneField(Utilisateur, on_delete = models.CASCADE, primary_key = True, verbose_name = "Compte utilisateur")
    date_de_creation = models.DateTimeField(auto_now_add = True, null = False, blank = False, verbose_name = "Date de création")

    # Définition des méthodes et sous classes
    def __str__(self):

        return str(self.compte_agent_de_reception.email)
    
    class Meta:

        verbose_name = 'Agent de réception'
        verbose_name_plural = 'Agents de réceptions'

        ordering = ["-date_de_creation"]

class Agent_Regisseur(models.Model):
    # Docstring de la classe
    """

        Résumé :

            --  Cette classe models intitulée Agent_Regisseur représente en base de données la table des
            --  Profils des agents régisseurs du système.

        Attributs :

            --  nom : Représente le nom du profil de l'agent régisseur
            --  prenoms : Représente le/les prénoms de l'agent régisseur
            --  photo_de_profil : Représente la photo de profil de l'agent régisseur
            --  compte_agent_regisseur : Représente le compte rattaché au profil de l'agent régisseur
            --  date_de_creation : Représente la date de création du profil de l'agent régisseur

    """

    nom = models.CharField(max_length = 50, null = False, blank = False, verbose_name = "Nom de l'agent régisseur")
    prenoms = models.CharField(max_length = 150, null = False, blank = False, verbose_name = "Prénom (s) de l'agent régisseur")
    photo_de_profil = models.ImageField(upload_to = "photos_de_profils_agents_regisseurs/", null = False, blank = False, validators = [FileExtensionValidator(allowed_extensions = ["jpg", "png", "jpeg",])], verbose_name = "Photo de profil de l'agent régisseur")
    compte_agent_regisseur = models.OneToOneField(Utilisateur, on_delete = models.CASCADE, primary_key = True, verbose_name = "Compte utilisateur")
    date_de_creation = models.DateTimeField(auto_now_add = True, null = False, blank = False, verbose_name = "Date de création")

    # Définition des méthodes et sous classes
    def __str__(self):

        return str(self.compte_agent_regisseur.email)
    
    class Meta:

        verbose_name = 'Agent régisseur'
        verbose_name_plural = 'Agents régisseurs'

        ordering = ["-date_de_creation"]

class Agent_Charge_De_Diplome(models.Model):
    # Docstring de la classe
    """

        Résumé :

            --  Cette classe models intitulée Agent_Charge_De_Diplome représente en base de données la table des
            --  Profils des agents chargés de diplomes du système.

        Attributs :

            --  nom : Représente le nom du profil de l'agent chargé de diplome
            --  prenoms : Représente le/les prénoms de l'agent chargé de diplome
            --  photo_de_profil : Représente la photo de profil de l'agent chargé de diplome
            --  compte_agent_charge_de_diplome : Représente le compte rattaché au profil de l'agent chargé de diplome
            --  date_de_creation : Représente la date de création du profil de l'agent chargé de diplome

    """

    nom = models.CharField(max_length = 50, null = False, blank = False, verbose_name = "Nom de l'agent chargé de diplome")
    prenoms = models.CharField(max_length = 150, null = False, blank = False, verbose_name = "Prénom (s) de l'agent chargé de diplome")
    photo_de_profil = models.ImageField(upload_to = "photos_de_profils_agents_charges_de_diplomes/", null = False, blank = False, validators = [FileExtensionValidator(allowed_extensions = ["jpg", "png", "jpeg",])], verbose_name = "Photo de profil de l'agent chargé de diplome")
    compte_agent_charge_de_diplome = models.OneToOneField(Utilisateur, on_delete = models.CASCADE, primary_key = True, verbose_name = "Compte utilisateur")
    date_de_creation = models.DateTimeField(auto_now_add = True, null = False, blank = False, verbose_name = "Date de création")

    # Définition des méthodes et sous classes
    def __str__(self):

        return str(self.compte_agent_charge_de_diplome.email)
    
    class Meta:

        verbose_name = 'Agent chargé de diplome'
        verbose_name_plural = 'Agents chargés de diplomes'

        ordering = ["-date_de_creation"]

class Agent_De_Verification(models.Model):
    # Docstring de la classe
    """

        Résumé :

            --  Cette classe models intitulée Agent_De_Verification représente en base de données la table des
            --  Profils des agents de vérifications du système.

        Attributs :

            --  nom : Représente le nom du profil de l'agent de vérification
            --  prenoms : Représente le/les prénoms de l'agent de vérification
            --  photo_de_profil : Représente la photo de profil de l'agent de vérification
            --  compte_agent_de_verification : Représente le compte rattaché au profil de l'agent de vérification
            --  date_de_creation : Représente la date de création du profil de l'agent de vérification

    """

    nom = models.CharField(max_length = 50, null = False, blank = False, verbose_name = "Nom de l'agent de vérification")
    prenoms = models.CharField(max_length = 150, null = False, blank = False, verbose_name = "Prénom (s) de l'agent de vérification")
    photo_de_profil = models.ImageField(upload_to = "photos_de_profils_agents_de_verifications/", null = False, blank = False, validators = [FileExtensionValidator(allowed_extensions = ["jpg", "png", "jpeg",])], verbose_name = "Photo de profil de l'agent de vérification")
    compte_agent_de_verification = models.OneToOneField(Utilisateur, on_delete = models.CASCADE, primary_key = True, verbose_name = "Compte utilisateur")
    date_de_creation = models.DateTimeField(auto_now_add = True, null = False, blank = False, verbose_name = "Date de création")

    # Définition des méthodes et sous classes
    def __str__(self):

        return str(self.compte_agent_de_verification.email)
    
    class Meta:

        verbose_name = 'Agent de vérification'
        verbose_name_plural = 'Agents de vérifications'

        ordering = ["-date_de_creation"]

class Agent_De_Production(models.Model):
    # Docstring de la classe
    """

        Résumé :

            --  Cette classe models intitulée Agent_De_Production représente en base de données la table des
            --  Profils des agents de productions du système.

        Attributs :

            --  nom : Représente le nom du profil de l'agent de production
            --  prenoms : Représente le/les prénoms de l'agent de production
            --  photo_de_profil : Représente la photo de profil de l'agent de production
            --  compte_agent_de_production : Représente le compte rattaché au profil de l'agent de production
            --  date_de_creation : Représente la date de création du profil de l'agent de production

    """
    nom = models.CharField(max_length = 50, null = False, blank = False, verbose_name = "Nom de l'agent de production")
    prenoms = models.CharField(max_length = 150, null = False, blank = False, verbose_name = "Prénom (s) de l'agent de production")
    photo_de_profil = models.ImageField(upload_to = "photos_de_profils_agents_de_productions/", null = False, blank = False, validators = [FileExtensionValidator(allowed_extensions = ["jpg", "png", "jpeg",])], verbose_name = "Photo de profil de l'agent de production")
    compte_agent_de_production = models.OneToOneField(Utilisateur, on_delete = models.CASCADE, primary_key = True, verbose_name = "Compte utilisateur")
    date_de_creation = models.DateTimeField(auto_now_add = True, null = False, blank = False, verbose_name = "Date de création")

    # Définition des méthodes et sous classes
    def __str__(self):

        return str(self.compte_agent_de_production.email)
    
    class Meta:

        verbose_name = 'Agent de production'
        verbose_name_plural = 'Agents de productions'

        ordering = ["-date_de_creation"]

class Agent_De_Distribution(models.Model):
    # Docstring de la classe
    """

        Résumé :

            --  Cette classe models intitulée Agent_De_Distribution représente en base de données la table des
            --  Profils des agents de distributions du système.

        Attributs :

            --  nom : Représente le nom du profil de l'agent de distribution
            --  prenoms : Représente le/les prénoms de l'agent de distribution
            --  photo_de_profil : Représente la photo de profil de l'agent de distribution
            --  compte_agent_de_distribution : Représente le compte rattaché au profil de l'agent de distribution
            --  date_de_creation : Représente la date de création du profil de l'agent de distribution

    """
    nom = models.CharField(max_length = 50, null = False, blank = False, verbose_name = "Nom de l'agent de distribution")
    prenoms = models.CharField(max_length = 150, null = False, blank = False, verbose_name = "Prénom (s) de l'agent de distribution")
    photo_de_profil = models.ImageField(upload_to = "photos_de_profils_agents_de_distributions/", null = False, blank = False, validators = [FileExtensionValidator(allowed_extensions = ["jpg", "png", "jpeg",])], verbose_name = "Photo de profil de l'agent de distribution")
    compte_agent_de_distribution = models.OneToOneField(Utilisateur, on_delete = models.CASCADE, primary_key = True, verbose_name = "Compte utilisateur")
    date_de_creation = models.DateTimeField(auto_now_add = True, null = False, blank = False, verbose_name = "Date de création")

    # Définition des méthodes et sous classes
    def __str__(self):

        return str(self.compte_agent_de_distribution.email)
    
    class Meta:

        verbose_name = 'Agent de distribution'
        verbose_name_plural = 'Agents de distributions'

        ordering = ["-date_de_creation"]
        