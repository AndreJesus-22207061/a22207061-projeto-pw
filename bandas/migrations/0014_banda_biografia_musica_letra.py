# Generated by Django 4.0.6 on 2024-05-20 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0013_alter_album_musicas'),
    ]

    operations = [
        migrations.AddField(
            model_name='banda',
            name='biografia',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='musica',
            name='letra',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
