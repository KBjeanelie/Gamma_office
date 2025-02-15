# Generated by Django 5.0.2 on 2024-05-07 23:34

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Demandes', '0003_alter_demande_bac_date_de_naissance_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='demande_bac',
            name='copie_couleur_d_une_piece_d_identite',
            field=models.FileField(blank=True, null=True, upload_to='copies_couleurs_des_pieces_d_identites/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])], verbose_name="Copie couleur de la pièce d'identité"),
        ),
        migrations.AlterField(
            model_name='demande_bac',
            name='copie_couleur_de_l_acte_de_naissance',
            field=models.FileField(blank=True, null=True, upload_to='copies_couleurs_des_actes_de_naissances/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])], verbose_name="Copie couleur de l'acte de naissance"),
        ),
        migrations.AlterField(
            model_name='demande_bac',
            name='copie_couleur_du_bepc',
            field=models.FileField(blank=True, null=True, upload_to='copies_couleurs_des_bepc/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])], verbose_name='Copie couleur du BEPC'),
        ),
        migrations.AlterField(
            model_name='demande_bepc',
            name='copie_couleur_d_une_piece_d_identite',
            field=models.FileField(blank=True, null=True, upload_to='copies_couleurs_des_pieces_d_identites/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])], verbose_name="Copie couleur de la pièce d'identité"),
        ),
        migrations.AlterField(
            model_name='demande_bepc',
            name='copie_couleur_de_l_acte_de_naissance',
            field=models.FileField(blank=True, null=True, upload_to='copies_couleurs_des_actes_de_naissances/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])], verbose_name="Copie couleur de l'acte de naissance"),
        ),
        migrations.AlterField(
            model_name='demande_bepc',
            name='copie_couleur_du_cepe',
            field=models.FileField(blank=True, null=True, upload_to='copies_couleurs_des_cepe/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])], verbose_name='Copie couleur du CEPE'),
        ),
        migrations.AlterField(
            model_name='demande_cepe',
            name='copie_couleur_d_une_piece_d_identite',
            field=models.FileField(blank=True, null=True, upload_to='copies_couleurs_des_pieces_d_identites/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])], verbose_name="Copie couleur de la pièce d'identité"),
        ),
        migrations.AlterField(
            model_name='demande_cepe',
            name='copie_couleur_de_l_acte_de_naissance',
            field=models.FileField(blank=True, null=True, upload_to='copies_couleurs_des_actes_de_naissances/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])], verbose_name="Copie couleur de l'acte de naissance"),
        ),
        migrations.CreateModel(
            name='Activites_Demande_Bac',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_de_traitement', models.CharField(choices=[('Création', 'Création'), ('Modification', 'Modification'), ('Suppression', 'Suppression'), ('Consultation', 'Consultation')], default='Création', max_length=50, verbose_name='Type de traitement')),
                ('date_de_traitement', models.DateTimeField(auto_now_add=True, verbose_name='Date de traitement')),
                ('demande', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Demandes.demande_bac', verbose_name='Demande')),
                ('utilisateur', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Utilisateur')),
            ],
            options={
                'verbose_name': 'Activité de demande BAC',
                'verbose_name_plural': 'Activités des demandes BAC',
                'ordering': ['-date_de_traitement'],
            },
        ),
        migrations.CreateModel(
            name='Activites_Demande_Bepc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_de_traitement', models.CharField(choices=[('Création', 'Création'), ('Modification', 'Modification'), ('Suppression', 'Suppression'), ('Consultation', 'Consultation')], default='Création', max_length=50, verbose_name='Type de traitement')),
                ('date_de_traitement', models.DateTimeField(auto_now_add=True, verbose_name='Date de traitement')),
                ('demande', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Demandes.demande_bepc', verbose_name='Demande')),
                ('utilisateur', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Utilisateur')),
            ],
            options={
                'verbose_name': 'Activité de demande BEPC',
                'verbose_name_plural': 'Activités des demandes BEPC',
                'ordering': ['-date_de_traitement'],
            },
        ),
        migrations.CreateModel(
            name='Activites_Demande_Cepe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_de_traitement', models.CharField(choices=[('Création', 'Création'), ('Modification', 'Modification'), ('Suppression', 'Suppression'), ('Consultation', 'Consultation')], default='Création', max_length=50, verbose_name='Type de traitement')),
                ('date_de_traitement', models.DateTimeField(auto_now_add=True, verbose_name='Date de traitement')),
                ('demande', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Demandes.demande_cepe', verbose_name='Demande')),
                ('utilisateur', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Utilisateur')),
            ],
            options={
                'verbose_name': 'Activité de demande CEPE',
                'verbose_name_plural': 'Activités des demandes CEPE',
                'ordering': ['-date_de_traitement'],
            },
        ),
    ]
