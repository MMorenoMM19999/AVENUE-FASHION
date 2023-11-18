# Generated by Django 4.2.7 on 2023-11-16 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("Application", "0002_alter_asesorcomercial_id_asesor_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="asesorcomercial",
            name="id_usuario",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="Application.usuario",
            ),
        ),
        migrations.AlterField(
            model_name="gerente",
            name="id_usuario",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="Application.usuario",
            ),
        ),
        migrations.AlterField(
            model_name="jefetaller",
            name="id_usuario",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="Application.usuario",
            ),
        ),
    ]