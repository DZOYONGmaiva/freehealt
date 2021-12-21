# Generated by Django 3.2.8 on 2021-11-29 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('RendezVous', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ordonnance',
            fields=[
                ('idOrdonnance', models.AutoField(primary_key=True, serialize=False)),
                ('idRenvezvousOr', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='RendezVous.rendezvous')),
            ],
        ),
    ]
