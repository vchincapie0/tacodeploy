# Generated by Django 5.0.2 on 2024-06-01 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productoterminado', '0003_productoterminadogenerico_cantidad_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='productoterminadogenerico',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]