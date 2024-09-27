# Generated by Django 5.1.1 on 2024-09-22 07:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CatedraAdultoMayor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactoEmergencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_familiar', models.CharField(max_length=100)),
                ('relacion', models.CharField(max_length=50)),
                ('numero_telefono', models.CharField(max_length=15)),
                ('anciano', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contactos', to='CatedraAdultoMayor.anciano')),
            ],
        ),
    ]
