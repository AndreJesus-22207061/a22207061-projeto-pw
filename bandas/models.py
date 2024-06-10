from django.db import models


class Album(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    ano_lancamento = models.IntegerField(null=True)
    banda = models.ForeignKey('Banda', on_delete=models.CASCADE, null=True, blank=True, related_name='albuns')
    musicas = models.ManyToManyField('Musica', related_name='albums',null=True, blank=True,)
    capa = models.ImageField(upload_to="capas", null=True, blank=True, default=None)

    def __str__(self):
        return f"{self.nome} - {self.banda}"

class Musica(models.Model):
    id = models.AutoField(primary_key=True)
    spotify_link = models.URLField(blank=True, null=True, default=None)
    nome = models.CharField(max_length=100)
    tempo = models.CharField(max_length=100)
    letra = models.TextField(default='', null=True, blank=True)

    def __str__(self):
        return f"{self.nome}"

class Banda(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    nacionalidade = models.CharField(max_length=100, null=True)
    ano_criacao = models.IntegerField(null=True)
    biografia = models.TextField(default='', null=True, blank=True)
    foto = models.ImageField(upload_to="fotos", null=True, blank=True, default=None)

    def __str__(self):
        return self.nome


