# Generated by Django 4.2.7 on 2024-01-14 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Facturacion', '0004_alter_ingrediente_cantidad_disponible_bg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receta',
            name='cantidad_bg',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='receta',
            name='procedimiento_bg',
            field=models.CharField(max_length=500),
        ),
    ]