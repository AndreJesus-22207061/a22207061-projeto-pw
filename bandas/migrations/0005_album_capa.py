# Generated by Django 4.0.6 on 2024-04-17 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0004_alter_album_banda'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='capa',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='capas'),
        ),
    ]
