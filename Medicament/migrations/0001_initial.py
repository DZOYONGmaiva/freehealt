# Generated by Django 3.2.8 on 2021-11-29 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medicament',
            fields=[
                ('idMedicament', models.AutoField(primary_key=True, serialize=False)),
                ('nomMedicament', models.CharField(max_length=15)),
                ('quantiteEnStock', models.IntegerField()),
                ('prixMedicament', models.FloatField()),
                ('descriptionMedicament', models.TextField()),
            ],
        ),
    ]
