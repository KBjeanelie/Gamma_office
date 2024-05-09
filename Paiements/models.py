# Encodage du fichier
#coding: utf-8

# Importations des modules
from django.db import models
from Demandes.models import *

# Définitions des classes Models
class Paiements_Demande_Bac(models.Model):
    # Docstring de la classe
    """

        Résumé :

            --  Cette classe models intitulée Paiements_Demande_Bac représente en base de données la table
            --  Des paiements effectués des demandes BAC.

        Attributs :

            --  demande : Représente la demande payée
            --  montant : Représente le montant payé
            --  type_de_paiement : Représente le type de paiement
            --  date_de_paiement : Représente la date et l'heure de paiement de la demande
    
    """

    # Liste de type de paiement de la demande
    EN_ESPECE = "En espèce"
    VIA_DIGIDEC = "Via digidec lite"

    TYPE_PAIEMENT = [
        (EN_ESPECE, 'En espèce'),
        (VIA_DIGIDEC, 'Via digidec lite'),
    ]

    demande = models.OneToOneField(Demande_Bac, on_delete = models.CASCADE, primary_key = True, null = False, blank = False,verbose_name = "Demande")
    montant = models.CharField(max_length = 50, null = False, blank = False, verbose_name = "Montant")
    type_de_paiement = models.CharField(max_length = 50, null = False, blank = False, choices = TYPE_PAIEMENT, default = EN_ESPECE, verbose_name = "Type de paiement")
    date_de_paiement = models.DateTimeField(auto_now_add = True, null = False, blank = False, verbose_name = "Date de paiement")

    # Définition des méthodes et sous classes
    def __str__(self):

        return str(self.date_de_paiement)
    
    class Meta:

        verbose_name = 'Paiement de demande BAC'
        verbose_name_plural = 'Paiements des demandes BAC'

        ordering = ["-date_de_paiement"]

class Paiements_Demande_Bepc(models.Model):
    # Docstring de la classe
    """

        Résumé :

            --  Cette classe models intitulée Paiements_Demande_Bepc représente en base de données la table
            --  Des paiements effectués des demandes BEPC.

        Attributs :

            --  demande : Représente la demande payée
            --  montant : Représente le montant payé
            --  type_de_paiement : Représente le type de paiement
            --  date_de_paiement : Représente la date et l'heure de paiement de la demande
    
    """

    # Liste de type de paiement de la demande
    EN_ESPECE = "En espèce"
    VIA_DIGIDEC = "Via digidec lite"

    TYPE_PAIEMENT = [
        (EN_ESPECE, 'En espèce'),
        (VIA_DIGIDEC, 'Via digidec lite'),
    ]

    demande = models.OneToOneField(Demande_Bepc, on_delete = models.CASCADE, primary_key = True, null = False, blank = False,verbose_name = "Demande")
    montant = models.CharField(max_length = 50, null = False, blank = False, verbose_name = "Montant")
    type_de_paiement = models.CharField(max_length = 50, null = False, blank = False, choices = TYPE_PAIEMENT, default = EN_ESPECE, verbose_name = "Type de paiement")
    date_de_paiement = models.DateTimeField(auto_now_add = True, null = False, blank = False, verbose_name = "Date de paiement")

    # Définition des méthodes et sous classes
    def __str__(self):

        return str(self.date_de_paiement)
    
    class Meta:

        verbose_name = 'Paiement de demande BEPC'
        verbose_name_plural = 'Paiements des demandes BEPC'

        ordering = ["-date_de_paiement"]

class Paiements_Demande_Cepe(models.Model):
    # Docstring de la classe
    """

        Résumé :

            --  Cette classe models intitulée Paiements_Demande_Cepe représente en base de données la table
            --  Des paiements effectués des demandes CEPE.

        Attributs :

            --  demande : Représente la demande payée
            --  montant : Représente le montant payé
            --  type_de_paiement : Représente le type de paiement
            --  date_de_paiement : Représente la date et l'heure de paiement de la demande
    
    """

    # Liste de type de paiement de la demande
    EN_ESPECE = "En espèce"
    VIA_DIGIDEC = "Via digidec lite"

    TYPE_PAIEMENT = [
        (EN_ESPECE, 'En espèce'),
        (VIA_DIGIDEC, 'Via digidec lite'),
    ]

    demande = models.OneToOneField(Demande_Cepe, on_delete = models.CASCADE, primary_key = True, null = False, blank = False,verbose_name = "Demande")
    montant = models.CharField(max_length = 50, null = False, blank = False, verbose_name = "Montant")
    type_de_paiement = models.CharField(max_length = 50, null = False, blank = False, choices = TYPE_PAIEMENT, default = EN_ESPECE, verbose_name = "Type de paiement")
    date_de_paiement = models.DateTimeField(auto_now_add = True, null = False, blank = False, verbose_name = "Date de paiement")

    # Définition des méthodes et sous classes
    def __str__(self):

        return str(self.date_de_paiement)
    
    class Meta:

        verbose_name = 'Paiement de demande CEPE'
        verbose_name_plural = 'Paiements des demandes CEPE'

        ordering = ["-date_de_paiement"]