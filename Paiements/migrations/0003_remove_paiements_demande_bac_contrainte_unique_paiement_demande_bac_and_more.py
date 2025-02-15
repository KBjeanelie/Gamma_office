# Generated by Django 5.0.2 on 2024-05-08 00:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Demandes', '0005_activites_demande_bac_contrainte_unique_activite_demande_bac_and_more'),
        ('Paiements', '0002_remove_paiements_demande_bac_contrainte_unique_paiement_demande_bac_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='paiements_demande_bac',
            name='contrainte_unique_paiement_demande_bac',
        ),
        migrations.RemoveConstraint(
            model_name='paiements_demande_bepc',
            name='contrainte_unique_paiement_demande_bepc',
        ),
        migrations.RemoveConstraint(
            model_name='paiements_demande_cepe',
            name='contrainte_unique_paiement_demande_cepe',
        ),
        migrations.AlterField(
            model_name='paiements_demande_bac',
            name='demande',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Demandes.demande_bac', unique=True, verbose_name='Demande'),
        ),
        migrations.AlterField(
            model_name='paiements_demande_bepc',
            name='demande',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Demandes.demande_bepc', unique=True, verbose_name='Demande'),
        ),
        migrations.AlterField(
            model_name='paiements_demande_cepe',
            name='demande',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Demandes.demande_cepe', unique=True, verbose_name='Demande'),
        ),
    ]
