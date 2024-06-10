from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()


    def __str__(self):
        return f'{self.nome} - {self.idade} anos'
