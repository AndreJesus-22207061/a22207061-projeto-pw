# Generated by Django 4.0.6 on 2024-04-18 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0010_album_capa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musica',
            name='tempo',
            field=models.CharField(max_length=100),
        ),
    ]
