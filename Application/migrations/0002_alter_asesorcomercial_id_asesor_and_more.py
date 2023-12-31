# Generated by Django 4.2.7 on 2023-11-16 00:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Application", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="asesorcomercial",
            name="id_asesor",
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="cliente",
            name="id_cliente",
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="empleado",
            name="id_empleado",
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="gerente",
            name="id_gerente",
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="jefetaller",
            name="id_jefetaller",
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="sucursal",
            name="cod_sucursal",
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
