# Generated by Django 4.2.7 on 2023-11-06 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0003_alter_fotos_bd_comentario_alter_fotos_bd_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fotos_bd',
            name='comentario',
        ),
        migrations.RemoveField(
            model_name='fotos_bd',
            name='like',
        ),
    ]
