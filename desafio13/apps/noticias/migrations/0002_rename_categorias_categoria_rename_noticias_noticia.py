# Generated by Django 4.2.3 on 2023-07-19 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categorias',
            new_name='Categoria',
        ),
        migrations.RenameModel(
            old_name='Noticias',
            new_name='Noticia',
        ),
    ]
