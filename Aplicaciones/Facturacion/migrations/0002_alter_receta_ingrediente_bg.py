# Generated by Django 4.2.7 on 2024-01-12 23:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Facturacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receta',
            name='ingrediente_bg',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Facturacion.ingrediente'),
        ),
    ]
