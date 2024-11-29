# Generated by Django 5.1.3 on 2024-11-29 03:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mesa', models.CharField(max_length=10)),
                ('estado', models.CharField(choices=[('Pendiente', 'Pendiente'), ('En Preparación', 'En Preparación'), ('Listo', 'Listo'), ('Pagado', 'Pagado'), ('Cerrado', 'Cerrado')], default='Pendiente', max_length=20)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('mesero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Platillo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=6)),
                ('areas', models.ManyToManyField(to='core.area')),
            ],
        ),
        migrations.CreateModel(
            name='Parte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(choices=[('Pendiente', 'Pendiente'), ('Preparando', 'Preparando'), ('Listo', 'Listo'), ('Completado', 'Completado')], default='Pendiente', max_length=20)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.area')),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partes', to='core.pedido')),
                ('platillo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.platillo')),
            ],
        ),
    ]
