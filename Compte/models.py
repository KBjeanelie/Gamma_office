# Encodage du fichier
#coding: utf-8

# Importations des modules
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

# Redéfinition des classes Models
class UserManager(BaseUserManager):
    
    def create_user(self, email, password = None, **extra_fields):
        
        if not email:

            raise ValueError('Les utilisateurs doivent avoir une adresse email')

        user = self.model(email = email, **extra_fields)

        user.set_password(password)
        user.save(using = self._db)

        return user

    def create_superuser(self, email, password = None, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        user = self.create_user(email, password = password, **extra_fields)

        user.save(using = self._db)

        return user
    
class Utilisateur(AbstractBaseUser, PermissionsMixin):
    # Docstring de la classe
    """

        Résumé :

            --  Cette classe model intitulée Utilisateur représente en base de données la table
            --  Des comptes des utilisateurs du système.

        Attributs :

            --  email : Représente l'adresse email rattachée au compte d'un utilisateur
            --  statut_agent_reception : Représente un drapeau signifiant que le compte appartient à un agent de réception
            --  statut_agent_regisseur : Représente un drapeau signifiant que le compte appartient à un agent régisseur
            --  statut_agent_charge_de_diplome : Représente un drapeau signifiant que le compte appartient à un agent chargé de diplome
            --  statut_agent_de_verification : Représente un drapeau signifiant que le compte appartient à un agent de vérification
            --  statut_agent_de_production : Représente un drapeau signifiant que le compte appartient à un agent de production
            --  statut_agent_de_distribution : Représente un drapeau signifiant que le compte appartient à un agent de distribution
            --  is_active : Représente un drapeau signifiant que le compte utilisateur est actif
            --  is_staff : Représente un drapeau signifiant que le compte utilisateur peut se connecter au site d'administration
            --  last_login : Représente la dernière date et heure de connexion de l'utilisateur
            --  date_joined : Représente la date et heure de création du compte
    
    """
    
    email = models.EmailField(null = False, blank = False, default = False, max_length = 254, unique = True, verbose_name = 'Adresse email')
    statut_agent_reception = models.BooleanField(null = False, blank = False, default = False, verbose_name = "Agent de réception")
    statut_agent_regisseur = models.BooleanField(null = False, blank = False, default = False, verbose_name = "Agent régisseur")
    statut_agent_charge_de_diplome = models.BooleanField(null = False, blank = False, default = False, verbose_name = "Agent chargé de diplome")
    statut_agent_de_verification = models.BooleanField(null = False, blank = False, default = False, verbose_name = "Agent de vérification")
    statut_agent_de_production = models.BooleanField(null = False, blank = False, default = False, verbose_name = "Agent de production")
    statut_agent_de_distribution = models.BooleanField(null = False, blank = False, default = False, verbose_name = "Agent de distribution")
    is_active = models.BooleanField(default = True, null = False, blank = False, verbose_name = "Compte actif")
    is_staff = models.BooleanField(default = False, null = False, blank = False, verbose_name = "Compte administrateur")
    last_login = models.DateTimeField(blank = True, null = True, verbose_name = 'Dernière connexion')
    date_joined = models.DateTimeField(auto_now_add = True, null = False, blank = False, verbose_name = "Date de création")

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # Définitions des méthodes et sous classes
    def __str__(self):

        return str(self.email)
    
    class Meta:

        verbose_name = 'Utilisateur'
        verbose_name_plural = 'Utilisateurs'

        ordering = ["-date_joined"]
 