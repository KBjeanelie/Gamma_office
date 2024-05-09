# Encodage du fichier
#coding: utf-8

# Importations des modules
from django.db import models
from django.core.validators import FileExtensionValidator
from Compte.models import Utilisateur

# Définitions des classes Models
class Demande_Bac(models.Model):
    # Docstring de la classe
    """

        Résumé :

            --  Cette classe models intitulée Demande_Bac représente en base de données la table des
            --  Demandes Bac du système.

        Attributs :

            --  objet : Représente l'objet
            --  matricule : Représente le matricule
            --  nom : Représente le nom
            --  prenoms : Représente le/les prénoms
            --  date_de_naissance : Représente la date de naissance
            --  lieu_de_naissance : Représente le lieu de naissance
            --  numero_de_telephone : Représente le numéro de téléphone
            --  departement : Représente le département
            --  etablissement_d_origine : Représente l'établissement d'origine
            --  annee_d_obtention_du_bac : Représente l'année d'obtention du Bac
            --  copie_couleur_de_l_acte_de_naissance : Représente la copie couleur de l'acte de naissance
            --  copie_couleur_du_bepc : Représente la copie en couleur du Bepc
            --  copie_couleur_d_une_piece_d_identite : Représente une copie en couleur d'une pièce d'identité
            --  date_d_enregistrement : Représente la date d'enregistrement

    """

    # Liste d'objets de la demande
    DIPLOME = "Diplome BAC"
    ATTESTATION = "Attestation de réussite BAC"
    RELEVE = "Relevé de notes BAC"

    TYPE_OBJET = [
        (DIPLOME, 'Diplome BAC'),
        (ATTESTATION, 'Attestation de réussite BAC'),
        (RELEVE, 'Relevé de notes BAC'),
    ]

    
    objet = models.CharField(max_length = 50, null = False, blank = False, choices = TYPE_OBJET, default = DIPLOME, verbose_name = "Objet")
    matricule = models.CharField(max_length = 25, null = True, blank = True, default = "Matricule non renseigné", verbose_name = "Matricule")
    nom = models.CharField(max_length = 50, null = True, blank = True, default = "Nom non renseigné", verbose_name = "Nom")
    prenoms = models.CharField(max_length = 150, null = True, blank = True, default = "Prénoms non renseignés", verbose_name = "Prénoms")
    date_de_naissance = models.CharField(max_length = 50, null = True, blank = True, default = "Date de naissance non renseignée", verbose_name = "Date de naissance")
    lieu_de_naissance = models.CharField(max_length = 150, null = True, blank = True, default = "Lieu de naissance non renseigné", verbose_name = "Lieu de naissance")
    numero_de_telephone = models.CharField(max_length = 50, null = True, blank = True, default = "Numéro de téléphone non renseigné", verbose_name = "Numéro de téléphone")
    departement = models.CharField(max_length = 50, null = True, blank = True, default = "Département non renseigné", verbose_name = "Département")
    etablissement_d_origine = models.CharField(max_length = 150, null = True, blank = True, default = "Etablissement d'origine non renseigné", verbose_name = "Etablissement d'origine")
    annee_d_obtention_du_bac = models.CharField(max_length = 50, null = True, blank = True, default = "Année d'obtention du BAC non renseignée", verbose_name = "Année d'obtention du BAC")
    copie_couleur_de_l_acte_de_naissance = models.FileField(validators = [FileExtensionValidator(allowed_extensions = ["pdf",])], upload_to = "copies_couleurs_des_actes_de_naissances/", null = True, blank = True, verbose_name = "Copie couleur de l'acte de naissance")
    copie_couleur_du_bepc = models.FileField(validators = [FileExtensionValidator(allowed_extensions = ["pdf",])], upload_to = "copies_couleurs_des_bepc/", null = True, blank = True, verbose_name = "Copie couleur du BEPC")
    copie_couleur_d_une_piece_d_identite = models.FileField(validators = [FileExtensionValidator(allowed_extensions = ["pdf",])], upload_to = "copies_couleurs_des_pieces_d_identites/", null = True, blank = True, verbose_name = "Copie couleur de la pièce d'identité")
    date_d_enregistrement = models.DateTimeField(auto_now_add = True, null = False, blank = False, verbose_name = "Date d'enregistrement")

    # Définition des méthodes et sous classes
    def __str__(self):

        return str(self.date_d_enregistrement)
    
    class Meta:

        verbose_name = 'Demande BAC'
        verbose_name_plural = 'Demandes BAC'

        ordering = ["-date_d_enregistrement"]

class Activites_Demande_Bac(models.Model):
    # Docstring de la classe
    """

        Résumé :

            --  Cette classe models intitulée Activites_Demande_Bac représente en base de données la table
            --  Des activités effectuées sur les différentes demandes BAC.

        Attributs :

            --  demande : Représente la demande traitée
            --  utilisateur : Représente l'utilisateur traitant
            --  type_de_traitement : Représente le type de traitement effectué
            --  date_de_traitement : Représente la date et l'heure de traitement de la demande
    
    """

    # Liste de type de traitement de la demande
    CREATION = "Création"
    MODIFICATION = "Modification"
    SUPPRESSION = "Suppression"
    CONSULTATION = "Consultation"

    TYPE_TRAITEMENT = [
        (CREATION, 'Création'),
        (MODIFICATION, 'Modification'),
        (SUPPRESSION, 'Suppression'),
        (CONSULTATION, 'Consultation'),
    ]

    demande = models.ForeignKey(Demande_Bac, on_delete = models.CASCADE, null = False, blank = False,verbose_name = "Demande")
    utilisateur = models.ForeignKey(Utilisateur, on_delete = models.CASCADE, null = True, blank=True,verbose_name = "Utilisateur")
    type_de_traitement = models.CharField(max_length = 50, null = False, blank = False, choices = TYPE_TRAITEMENT, default = CREATION, verbose_name = "Type de traitement")
    date_de_traitement = models.DateTimeField(auto_now_add = True, null = False, blank = False, verbose_name = "Date de traitement")

    # Définition des méthodes et sous classes
    def __str__(self):

        return str(self.date_de_traitement)
    
    class Meta:

        verbose_name = 'Activité de demande BAC'
        verbose_name_plural = 'Activités des demandes BAC'

        ordering = ["-date_de_traitement"]

        constraints = [
            models.UniqueConstraint(fields = ['demande', 'utilisateur', 'type_de_traitement'], name = 'contrainte_unique_activite_demande_bac'),
        ] 

class Demande_Bepc(models.Model):
    # Docstring de la classe
    """

        Résumé :

            --  Cette classe models intitulée Demande_Bepc représente en base de données la table des
            --  Demandes Bepc du système.

        Attributs :

            --  objet : Représente l'objet
            --  matricule : Représente le matricule
            --  nom : Représente le nom
            --  prenoms : Représente le/les prénoms
            --  date_de_naissance : Représente la date de naissance
            --  lieu_de_naissance : Représente le lieu de naissance
            --  numero_de_telephone : Représente le numéro de téléphone
            --  departement : Représente le département
            --  etablissement_d_origine : Représente l'établissement d'origine
            --  annee_d_obtention_du_bepc : Représente l'année d'obtention du Bepc
            --  copie_couleur_de_l_acte_de_naissance : Représente la copie couleur de l'acte de naissance
            --  copie_couleur_du_cepe : Représente la copie en couleur du Cepe
            --  copie_couleur_d_une_piece_d_identite : Représente une copie en couleur d'une pièce d'identité
            --  date_d_enregistrement : Représente la date d'enregistrement

    """

    # Liste d'objets de la demande
    DIPLOME = "Diplome BEPC"
    ATTESTATION = "Attestation de réussite BEPC"
    RELEVE = "Relevé de notes BEPC"

    TYPE_OBJET = [
        (DIPLOME, 'Diplome BEPC'),
        (ATTESTATION, 'Attestation de réussite BEPC'),
        (RELEVE, 'Relevé de notes BEPC'),
    ]

    
    objet = models.CharField(max_length = 50, null = False, blank = False, choices = TYPE_OBJET, default = DIPLOME, verbose_name = "Objet")
    matricule = models.CharField(max_length = 25, null = True, blank = True, default = "Matricule non renseigné", verbose_name = "Matricule")
    nom = models.CharField(max_length = 50, null = True, blank = True, default = "Nom non renseigné", verbose_name = "Nom")
    prenoms = models.CharField(max_length = 150, null = True, blank = True, default = "Prénoms non renseignés", verbose_name = "Prénoms")
    date_de_naissance = models.CharField(max_length = 50, null = True, blank = True, default = "Date de naissance non renseignée", verbose_name = "Date de naissance")
    lieu_de_naissance = models.CharField(max_length = 150, null = True, blank = True, default = "Lieu de naissance non renseigné", verbose_name = "Lieu de naissance")
    numero_de_telephone = models.CharField(max_length = 50, null = True, blank = True, default = "Numéro de téléphone non renseigné", verbose_name = "Numéro de téléphone")
    departement = models.CharField(max_length = 50, null = True, blank = True, default = "Département non renseigné", verbose_name = "Département")
    etablissement_d_origine = models.CharField(max_length = 150, null = True, blank = True, default = "Etablissement d'origine non renseigné", verbose_name = "Etablissement d'origine")
    annee_d_obtention_du_bepc = models.CharField(max_length = 50, null = True, blank = True, default = "Année d'obtention du BEPC non renseignée", verbose_name = "Année d'obtention du BEPC")
    copie_couleur_de_l_acte_de_naissance = models.FileField(validators = [FileExtensionValidator(allowed_extensions = ["pdf",])], upload_to = "copies_couleurs_des_actes_de_naissances/", null = True, blank = True, verbose_name = "Copie couleur de l'acte de naissance")
    copie_couleur_du_cepe = models.FileField(validators = [FileExtensionValidator(allowed_extensions = ["pdf",])], upload_to = "copies_couleurs_des_cepe/", null = True, blank = True, verbose_name = "Copie couleur du CEPE")
    copie_couleur_d_une_piece_d_identite = models.FileField(validators = [FileExtensionValidator(allowed_extensions = ["pdf",])], upload_to = "copies_couleurs_des_pieces_d_identites/", null = True, blank = True, verbose_name = "Copie couleur de la pièce d'identité")
    date_d_enregistrement = models.DateTimeField(auto_now_add = True, null = False, blank = False, verbose_name = "Date d'enregistrement")

    # Définition des méthodes et sous classes
    def __str__(self):

        return str(self.date_d_enregistrement)
    
    class Meta:

        verbose_name = 'Demande BEPC'
        verbose_name_plural = 'Demandes BEPC'

        ordering = ["-date_d_enregistrement"]

class Activites_Demande_Bepc(models.Model):
    # Docstring de la classe
    """

        Résumé :

            --  Cette classe models intitulée Activites_Demande_Bepc représente en base de données la table
            --  Des activités effectuées sur les différentes demandes BEPC.

        Attributs :

            --  demande : Représente la demande traitée
            --  utilisateur : Représente l'utilisateur traitant
            --  type_de_traitement : Représente le type de traitement effectué
            --  date_de_traitement : Représente la date et l'heure de traitement de la demande
    
    """

    # Liste de type de traitement de la demande
    CREATION = "Création"
    MODIFICATION = "Modification"
    SUPPRESSION = "Suppression"
    CONSULTATION = "Consultation"

    TYPE_TRAITEMENT = [
        (CREATION, 'Création'),
        (MODIFICATION, 'Modification'),
        (SUPPRESSION, 'Suppression'),
        (CONSULTATION, 'Consultation'),
    ]

    demande = models.ForeignKey(Demande_Bepc, on_delete = models.CASCADE, null = False, blank = False,verbose_name = "Demande")
    utilisateur = models.ForeignKey(Utilisateur, on_delete = models.CASCADE, null = True, blank=True,verbose_name = "Utilisateur")
    type_de_traitement = models.CharField(max_length = 50, null = False, blank = False, choices = TYPE_TRAITEMENT, default = CREATION, verbose_name = "Type de traitement")
    date_de_traitement = models.DateTimeField(auto_now_add = True, null = False, blank = False, verbose_name = "Date de traitement")

    # Définition des méthodes et sous classes
    def __str__(self):

        return str(self.date_de_traitement)
    
    class Meta:

        verbose_name = 'Activité de demande BEPC'
        verbose_name_plural = 'Activités des demandes BEPC'

        ordering = ["-date_de_traitement"]

        constraints = [
            models.UniqueConstraint(fields = ['demande', 'utilisateur', 'type_de_traitement'], name = 'contrainte_unique_activite_demande_bepc'),
        ] 

class Demande_Cepe(models.Model):
    # Docstring de la classe
    """

        Résumé :

            --  Cette classe models intitulée Demande_Cepe représente en base de données la table des
            --  Demandes Cepe du système.

        Attributs :

            --  objet : Représente l'objet
            --  matricule : Représente le matricule
            --  nom : Représente le nom
            --  prenoms : Représente le/les prénoms
            --  date_de_naissance : Représente la date de naissance
            --  lieu_de_naissance : Représente le lieu de naissance
            --  numero_de_telephone : Représente le numéro de téléphone
            --  departement : Représente le département
            --  etablissement_d_origine : Représente l'établissement d'origine
            --  annee_d_obtention_du_cepe : Représente l'année d'obtention du Cepe
            --  copie_couleur_de_l_acte_de_naissance : Représente la copie couleur de l'acte de naissance
            --  copie_couleur_d_une_piece_d_identite : Représente une copie en couleur d'une pièce d'identité
            --  date_d_enregistrement : Représente la date d'enregistrement

    """

    # Liste d'objets de la demande
    DIPLOME = "Diplome CEPE"
    ATTESTATION = "Attestation de réussite CEPE"
    RELEVE = "Relevé de notes CEPE"

    TYPE_OBJET = [
        (DIPLOME, 'Diplome CEPE'),
        (ATTESTATION, 'Attestation de réussite CEPE'),
        (RELEVE, 'Relevé de notes CEPE'),
    ]

    
    objet = models.CharField(max_length = 50, null = False, blank = False, choices = TYPE_OBJET, default = DIPLOME, verbose_name = "Objet")
    matricule = models.CharField(max_length = 25, null = True, blank = True, default = "Matricule non renseigné", verbose_name = "Matricule")
    nom = models.CharField(max_length = 50, null = True, blank = True, default = "Nom non renseigné", verbose_name = "Nom")
    prenoms = models.CharField(max_length = 150, null = True, blank = True, default = "Prénoms non renseignés", verbose_name = "Prénoms")
    date_de_naissance = models.CharField(max_length = 50, null = True, blank = True, default = "Date de naissance non renseignée", verbose_name = "Date de naissance")
    lieu_de_naissance = models.CharField(max_length = 150, null = True, blank = True, default = "Lieu de naissance non renseigné", verbose_name = "Lieu de naissance")
    numero_de_telephone = models.CharField(max_length = 50, null = True, blank = True, default = "Numéro de téléphone non renseigné", verbose_name = "Numéro de téléphone")
    departement = models.CharField(max_length = 50, null = True, blank = True, default = "Département non renseigné", verbose_name = "Département")
    etablissement_d_origine = models.CharField(max_length = 150, null = True, blank = True, default = "Etablissement d'origine non renseigné", verbose_name = "Etablissement d'origine")
    annee_d_obtention_du_cepe = models.CharField(max_length = 50, null = True, blank = True, default = "Année d'obtention du CEPE non renseignée", verbose_name = "Année d'obtention du CEPE")
    copie_couleur_de_l_acte_de_naissance = models.FileField(validators = [FileExtensionValidator(allowed_extensions = ["pdf",])], upload_to = "copies_couleurs_des_actes_de_naissances/", null = True, blank = True, verbose_name = "Copie couleur de l'acte de naissance")
    copie_couleur_d_une_piece_d_identite = models.FileField(validators = [FileExtensionValidator(allowed_extensions = ["pdf",])], upload_to = "copies_couleurs_des_pieces_d_identites/", null = True, blank = True, verbose_name = "Copie couleur de la pièce d'identité")
    date_d_enregistrement = models.DateTimeField(auto_now_add = True, null = False, blank = False, verbose_name = "Date d'enregistrement")

    # Définition des méthodes et sous classes
    def __str__(self):

        return str(self.date_d_enregistrement)
    
    class Meta:

        verbose_name = 'Demande CEPE'
        verbose_name_plural = 'Demandes CEPE'

        ordering = ["-date_d_enregistrement"]

class Activites_Demande_Cepe(models.Model):
    # Docstring de la classe
    """

        Résumé :

            --  Cette classe models intitulée Activites_Demande_Cepe représente en base de données la table
            --  Des activités effectuées sur les différentes demandes CEPE.

        Attributs :

            --  demande : Représente la demande traitée
            --  utilisateur : Représente l'utilisateur traitant
            --  type_de_traitement : Représente le type de traitement effectué
            --  date_de_traitement : Représente la date et l'heure de traitement de la demande
    
    """

    # Liste de type de traitement de la demande
    CREATION = "Création"
    MODIFICATION = "Modification"
    SUPPRESSION = "Suppression"
    CONSULTATION = "Consultation"

    TYPE_TRAITEMENT = [
        (CREATION, 'Création'),
        (MODIFICATION, 'Modification'),
        (SUPPRESSION, 'Suppression'),
        (CONSULTATION, 'Consultation'),
    ]

    demande = models.ForeignKey(Demande_Cepe, on_delete = models.CASCADE, null = False, blank = False,verbose_name = "Demande")
    utilisateur = models.ForeignKey(Utilisateur, on_delete = models.CASCADE, null = True, blank=True,verbose_name = "Utilisateur")
    type_de_traitement = models.CharField(max_length = 50, null = False, blank = False, choices = TYPE_TRAITEMENT, default = CREATION, verbose_name = "Type de traitement")
    date_de_traitement = models.DateTimeField(auto_now_add = True, null = False, blank = False, verbose_name = "Date de traitement")

    # Définition des méthodes et sous classes
    def __str__(self):

        return str(self.date_de_traitement)
    
    class Meta:

        verbose_name = 'Activité de demande CEPE'
        verbose_name_plural = 'Activités des demandes CEPE'

        ordering = ["-date_de_traitement"]

        constraints = [
            models.UniqueConstraint(fields = ['demande', 'utilisateur', 'type_de_traitement'], name = 'contrainte_unique_activite_demande_cepe'),
        ] 