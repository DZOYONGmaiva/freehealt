# Generated by Django 3.2.8 on 2021-11-29 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('UnePlageHoraireDuMedecin', '0001_initial'),
        ('Patient', '0001_initial'),
        ('PlageHoraire', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RendezVous',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idRendezVous', models.CharField(max_length=8, null=True)),
                ('dateReservation', models.DateField(auto_now_add=True, help_text='la date a laquelle la reservation est faite')),
                ('heureFinRDV', models.TimeField(blank=True, null=True)),
                ('status', models.CharField(max_length=1)),
                ('idMedecin', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='PlageHoraire.plagehoraire')),
                ('idPatientRDV', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Patient.patient')),
                ('idUnePlageHoraireDuMedecinRDV', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UnePlageHoraireDuMedecin.uneplagehorairedumedecin')),
            ],
        ),
    ]