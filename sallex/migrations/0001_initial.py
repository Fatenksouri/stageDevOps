# Generated by Django 5.0.6 on 2024-09-05 10:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Examen', '0001_initial'),
        ('Salle', '0003_alter_salle_id_examen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sallex',
            fields=[
                ('idse', models.AutoField(primary_key=True, serialize=False)),
                ('id_examen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Examen.examen')),
                ('id_salle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Salle.salle')),
            ],
        ),
    ]
