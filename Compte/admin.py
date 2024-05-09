# Encodage du fichier
#coding: utf-8

# Importations des modules
from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from Compte.models import Utilisateur

# Définitions des classes ModelForm
class UserCreationForm(forms.ModelForm):
    
    password1 = forms.CharField(label = 'Mot de passe', widget = forms.PasswordInput)
    password2 = forms.CharField(label = 'Confirmation du mot de passe', widget = forms.PasswordInput)

    class Meta:

        model = Utilisateur

        fields = ('email',)

    def clean_password2(self):
        
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:

            raise ValidationError("Les mots de passe ne correspondent pas.")
        
        return password2

    def save(self, commit = True):
        
        user = super().save(commit = False)
        user.set_password(self.cleaned_data["password1"])

        if commit:

            user.save()

        return user
    
class UserChangeForm(forms.ModelForm):
    
    password = ReadOnlyPasswordHashField()

    class Meta:

        model = Utilisateur

        fields = ('email', 'password', 'is_active', 'is_staff')

class UtilisateurAdmin(BaseUserAdmin):
    
    form = UserChangeForm

    add_form = UserCreationForm

    list_display = ('email', 'is_active', 'is_staff', 'is_superuser', 'statut_agent_reception', 'statut_agent_regisseur', 'statut_agent_charge_de_diplome', 'statut_agent_de_verification', 'statut_agent_de_production', 'statut_agent_de_distribution',)
    
    list_filter = ('is_active', 'is_staff', 'is_superuser', 'statut_agent_reception', 'statut_agent_regisseur', 'statut_agent_charge_de_diplome', 'statut_agent_de_verification', 'statut_agent_de_production', 'statut_agent_de_distribution',)

    fieldsets = (('Compte utilisateur', {'fields': ('email', 'password')}), ('Statut (s) du compte', {'fields': ('statut_agent_reception', 'statut_agent_regisseur', 'statut_agent_charge_de_diplome', 'statut_agent_de_verification', 'statut_agent_de_production', 'statut_agent_de_distribution',)}), ('Permission (s) du compte', {'fields': ('groups', 'user_permissions', 'is_staff', 'is_superuser', 'is_active',)}), ('Date de connexion', {'fields': ('last_login',)}),)
    
    add_fieldsets = ((None, {'classes': ('wide',), 'fields': ('email', 'password1', 'password2'),}),)
    
    search_fields = ('email',)

    ordering = ('-date_joined',)

admin.site.register(Utilisateur, UtilisateurAdmin)