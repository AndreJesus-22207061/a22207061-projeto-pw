# Generated by Django 4.0.6 on 2024-04-18 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0006_alter_album_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banda',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='musica',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
