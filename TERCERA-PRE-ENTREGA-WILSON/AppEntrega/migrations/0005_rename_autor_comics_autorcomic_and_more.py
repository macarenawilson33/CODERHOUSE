# Generated by Django 5.0.6 on 2024-06-02 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppEntrega', '0004_rename_banda_vinilo_artista'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comics',
            old_name='autor',
            new_name='AutorComic',
        ),
        migrations.RenameField(
            model_name='libro',
            old_name='autor',
            new_name='AutorLibro',
        ),
    ]