# Generated by Django 4.0.6 on 2024-05-17 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcurso', '0006_alter_projeto_disciplina'),
    ]

    operations = [
        migrations.AlterField(
            model_name='areacientifica',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='curso',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='disciplina',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='docente',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='linguagemdeprogramacao',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
