# Generated by Django 4.0.6 on 2024-04-17 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcurso', '0002_rename_curricular_unit_readable_code_disciplina_curriculariunitreadablecode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disciplina',
            name='linguagens',
            field=models.ManyToManyField(to='appcurso.linguagemdeprogramacao'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='linguagens',
            field=models.ManyToManyField(to='appcurso.linguagemdeprogramacao'),
        ),
    ]
