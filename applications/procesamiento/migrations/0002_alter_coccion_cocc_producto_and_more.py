# Generated by Django 5.0.2 on 2024-05-29 19:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('procesamiento', '0001_initial'),
        ('productoterminado', '0002_alter_caracteristicasorganolepticaspt_producto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coccion',
            name='cocc_producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productoterminado.productoterminadogenerico'),
        ),
        migrations.AlterField(
            model_name='picado',
            name='pica_producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productoterminado.productoterminadogenerico'),
        ),
    ]