# Generated by Django 5.0.7 on 2024-07-23 11:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Departement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unite',
            fields=[
                ('id_unite', models.AutoField(primary_key=True, serialize=False)),
                ('nom_unite', models.CharField(max_length=255)),
                ('id_departement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Departement.departement')),
            ],
        ),
    ]
