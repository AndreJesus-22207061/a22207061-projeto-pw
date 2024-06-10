from django.db import models

class AreaCientifica(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class LinguagemDeProgramacao(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Docente(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    disciplinas = models.ManyToManyField('Disciplina', related_name = 'docentes')

    def __str__(self):
        return self.nome

class Disciplina(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    ano = models.IntegerField()
    semestre = models.IntegerField()
    ects = models.IntegerField()
    apresentacao = models.TextField()
    programa = models.TextField()
    curricularIUnitReadableCode = models.CharField(max_length=20)
    area_cientifica = models.ForeignKey(AreaCientifica, on_delete=models.CASCADE, null = True, blank=True)
    linguagens = models.ManyToManyField('LinguagemDeProgramacao', null = True, blank=True)

    def __str__(self):
        return self.nome

class Projeto(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    disciplina = models.ForeignKey('Disciplina', on_delete=models.CASCADE, null = True, blank=True, related_name='projeto')
    descricao = models.TextField()
    conceitos_aplicados = models.TextField()
    tecnologias_usadas = models.TextField()
    foto_project = models.ImageField(upload_to='projeto_imagens/', null = True, blank=True)
    video_link = models.URLField(null = True, blank=True)
    project_link = models.URLField( null = True, blank=True)
    linguagens = models.ManyToManyField(LinguagemDeProgramacao, null = True, blank=True)

    def __str__(self):
        return self.nome

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    apresentacao = models.TextField()
    objetivos = models.TextField()
    competencias = models.TextField()
    capa =  models.ImageField(upload_to='curso_capa/', null = True, blank=True)

    def __str__(self):
        return self.nome
