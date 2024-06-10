from django.db import models


class Artigo(models.Model):
    id = models.AutoField(primary_key = True)
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey('Autor', on_delete=models.CASCADE, related_name='artigos_autor')
    conteudo = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)
    capa = models.ImageField(upload_to='artigos_photos/', null = True, blank = True, default = None)

    def __str__(self):
        return self.titulo

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    artigos = models.ManyToManyField('Artigo', related_name='categorias', null = True, blank = True)

    def __str__(self):
        return self.nome

class Comentario(models.Model):
    autor = models.ForeignKey('Autor', on_delete=models.CASCADE)
    artigo = models.ForeignKey('Artigo', on_delete=models.CASCADE)
    texto = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentário de {self.autor} em {self.artigo}"








class Rating(models.Model):
    artigo = models.ForeignKey('Artigo', on_delete=models.CASCADE)
    autor = models.ForeignKey('Autor', on_delete=models.CASCADE, default = 1)

    rate_possiveis=[

        (1 ,"1"),
        (2 ,"2"),
        (3 ,"3"),
        (4 ,"4"),
        (5 ,"5"),
        (6 ,"6"),
        (7 ,"7"),
        (8 ,"8"),
        (9 ,"9"),
        (10 ,"10")
    ]


    rating = models.IntegerField(choices = rate_possiveis)

    def __str__(self):
        return f"Tem uma avaliação de {self.rating} o artigo: {self.artigo}"

class Autor(models.Model):
    id = models.AutoField(primary_key = True)
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    email = models.URLField(blank=True, null=True)
    foto = models.ImageField(upload_to='autor_photos/' ,null = True, blank = True, default = None)


    def __str__(self):
        return self.nome
