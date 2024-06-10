# Generated by Django 4.0.6 on 2024-04-21 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogues', '0007_alter_autor_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='artigo',
            name='capa',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='artigos_photos/'),
        ),
        migrations.AlterField(
            model_name='autor',
            name='foto',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='autor_photos/'),
        ),
    ]
