# Generated by Django 4.2.6 on 2023-11-07 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0005_barra_pesquisa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentarios_bd',
            name='comentario',
            field=models.TextField(),
        ),
    ]
