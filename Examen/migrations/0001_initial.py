# Generated by Django 5.0.7 on 2024-07-23 11:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Module', '0001_initial'),
        ('Session', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Examen',
            fields=[
                ('id_examen', models.AutoField(primary_key=True, serialize=False)),
                ('nom_examen', models.CharField(max_length=255)),
                ('date_examen', models.DateField()),
                ('duree_examen', models.IntegerField()),
                ('type_examen', models.CharField(max_length=255)),
                ('id_module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Module.module')),
                ('id_session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Session.session')),
            ],
        ),
    ]
