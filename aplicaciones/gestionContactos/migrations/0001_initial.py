# Generated by Django 5.1.7 on 2025-03-30 23:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ciudad',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='empresa',
            fields=[
                ('nit_empresa', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('nombre_empresa', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='contacto_persona',
            fields=[
                ('id_contacto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_contacto', models.CharField(max_length=30)),
                ('apellido_contacto', models.CharField(max_length=30)),
                ('ciudad_contacto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionContactos.ciudad')),
                ('empresa_contacto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionContactos.empresa')),
            ],
        ),
        migrations.CreateModel(
            name='email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_contacto', models.EmailField(max_length=50)),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionContactos.contacto_persona')),
            ],
        ),
        migrations.CreateModel(
            name='telefono',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_telefono', models.CharField(max_length=15)),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionContactos.contacto_persona')),
            ],
        ),
    ]
